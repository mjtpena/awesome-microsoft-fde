// Everything the reference needs, in one readable file:
// monitoring, Azure AI Search, a Foundry account + project + model deployment,
// API Management as the AI gateway, one user-assigned identity for the app, and
// the role assignments that let each identity do exactly its job.
// Keys are disabled wherever the service allows it.

param location string
param tags object
param principalId string
param modelName string
param modelVersion string
param modelCapacity int
param tokensPerMinutePerCaller int
param apimPublisherEmail string

var suffix = uniqueString(resourceGroup().id)
var searchIndexName = 'harbourline-policies'
var modelDeploymentName = 'chat'

// Built-in role definition IDs (Azure RBAC built-in roles reference).
var roles = {
  cognitiveServicesOpenAIUser: '5e0bd9bd-7b93-4f28-af87-19fc36ad61bd'
  searchIndexDataReader: '1407120a-92aa-4202-b7e9-c0e197c71c8f'
  searchIndexDataContributor: '8ebe5a00-799e-43f5-93ac-243d3dce84a7'
  searchServiceContributor: '7ca78c08-252a-4471-8644-bb5ff32d4ba0'
  monitoringMetricsPublisher: '3913510d-42f4-4e42-8a64-420c390055eb'
}

// ---------------------------------------------------------------- monitoring

resource logs 'Microsoft.OperationalInsights/workspaces@2023-09-01' = {
  name: 'log-${suffix}'
  location: location
  tags: tags
  properties: {
    sku: { name: 'PerGB2018' }
    retentionInDays: 30 // agree the real retention with the records manager
  }
}

resource appInsights 'Microsoft.Insights/components@2020-02-02' = {
  name: 'appi-${suffix}'
  location: location
  tags: tags
  kind: 'web'
  properties: {
    Application_Type: 'web'
    WorkspaceResourceId: logs.id
    DisableLocalAuth: true // ingestion needs Entra auth; the gateway uses its managed identity
  }
}

// ------------------------------------------------------------------ identity

// The identity the assistant runs as wherever it is hosted (Container Apps,
// Functions, a VM). This reference doesn't deploy a host; attach this identity
// to yours and set AZURE_CLIENT_ID to its client ID.
resource appIdentity 'Microsoft.ManagedIdentity/userAssignedIdentities@2023-01-31' = {
  name: 'id-app-${suffix}'
  location: location
  tags: tags
}

// -------------------------------------------------------------------- search

resource search 'Microsoft.Search/searchServices@2025-05-01' = {
  name: 'srch-${suffix}'
  location: location
  tags: tags
  sku: { name: 'basic' }
  properties: {
    replicaCount: 1
    partitionCount: 1
    disableLocalAuth: true // Entra RBAC only; no admin or query keys
  }
}

// ------------------------------------------------------- Foundry and the model

resource foundry 'Microsoft.CognitiveServices/accounts@2025-06-01' = {
  name: 'aif-${suffix}'
  location: location
  tags: tags
  kind: 'AIServices'
  sku: { name: 'S0' }
  identity: { type: 'SystemAssigned' }
  properties: {
    allowProjectManagement: true
    customSubDomainName: 'aif-${suffix}' // required for Entra token auth
    disableLocalAuth: true // keys bypass RBAC, so turn them off
    publicNetworkAccess: 'Enabled' // landing-zone version: Disabled + private endpoint
  }
}

// Projects hold tracing, evaluations and agents. Nothing here needs it yet,
// but every Foundry feature you add next expects one.
resource project 'Microsoft.CognitiveServices/accounts/projects@2025-06-01' = {
  parent: foundry
  name: 'harbourline'
  location: location
  identity: { type: 'SystemAssigned' }
  properties: {}
}

resource model 'Microsoft.CognitiveServices/accounts/deployments@2025-06-01' = {
  parent: foundry
  name: modelDeploymentName
  sku: {
    name: 'GlobalStandard' // processes data in any region; use DataZoneStandard or Standard if residency matters
    capacity: modelCapacity
  }
  properties: {
    model: {
      format: 'OpenAI'
      name: modelName
      version: modelVersion
    }
  }
}

// ------------------------------------------------------- API Management gateway

resource apim 'Microsoft.ApiManagement/service@2024-05-01' = {
  name: 'apim-${suffix}'
  location: location
  tags: tags
  sku: {
    name: 'BasicV2' // v2 tiers deploy faster than classic; llm-token-limit supports Basic v2 and up
    capacity: 1
  }
  identity: { type: 'SystemAssigned' }
  properties: {
    publisherEmail: apimPublisherEmail
    publisherName: 'Harbourline (reference)'
  }
}

resource apimLogger 'Microsoft.ApiManagement/service/loggers@2024-05-01' = {
  parent: apim
  name: 'appinsights'
  properties: {
    loggerType: 'applicationInsights'
    resourceId: appInsights.id
    credentials: {
      connectionString: appInsights.properties.ConnectionString
      identityClientId: 'systemAssigned' // managed identity, because App Insights local auth is off
    }
  }
  dependsOn: [apimMetricsPublisher]
}

resource apimDiagnostics 'Microsoft.ApiManagement/service/diagnostics@2024-05-01' = {
  parent: apim
  name: 'applicationinsights'
  properties: {
    loggerId: apimLogger.id
    alwaysLog: 'allErrors'
    metrics: true // required for llm-emit-token-metric
    sampling: { samplingType: 'fixed', percentage: 100 }
    verbosity: 'information'
  }
}

resource backend 'Microsoft.ApiManagement/service/backends@2024-05-01' = {
  parent: apim
  name: 'foundry-models'
  properties: {
    protocol: 'http'
    url: '${foundry.properties.endpoint}openai'
    description: 'Foundry account, OpenAI-compatible endpoint'
  }
}

resource api 'Microsoft.ApiManagement/service/apis@2024-05-01' = {
  parent: apim
  name: 'models'
  properties: {
    displayName: 'Models (OpenAI-compatible)'
    path: 'openai' // gateway URL + /openai/v1/chat/completions maps to the account's /openai/v1/...
    protocols: ['https']
    subscriptionRequired: false // callers authenticate with Entra tokens, not subscription keys
  }
}

resource apiOperation 'Microsoft.ApiManagement/service/apis/operations@2024-05-01' = {
  parent: api
  name: 'post-all'
  properties: {
    displayName: 'POST any model operation'
    method: 'POST'
    urlTemplate: '/*'
  }
}

// Only these principals may call the gateway: the app identity and the person who ran azd.
var allowedOids = filter([appIdentity.properties.principalId, principalId], id => !empty(id))

resource apiPolicy 'Microsoft.ApiManagement/service/apis/policies@2024-05-01' = {
  parent: api
  name: 'policy'
  properties: {
    format: 'rawxml'
    value: replace(
      replace(
        replace(loadTextContent('apim-policy.xml'), '__TENANT_ID__', tenant().tenantId),
        '__ALLOWED_OIDS__',
        join(map(allowedOids, id => '<value>${id}</value>'), '')
      ),
      '__TOKENS_PER_MINUTE__',
      string(tokensPerMinutePerCaller)
    )
  }
  dependsOn: [backend, apimDiagnostics]
}

// ----------------------------------------------------------- audit trail

resource apimLogs 'Microsoft.Insights/diagnosticSettings@2021-05-01-preview' = {
  name: 'to-log-analytics'
  scope: apim
  properties: {
    workspaceId: logs.id
    logs: [{ categoryGroup: 'allLogs', enabled: true }]
  }
}

resource foundryLogs 'Microsoft.Insights/diagnosticSettings@2021-05-01-preview' = {
  name: 'to-log-analytics'
  scope: foundry
  properties: {
    workspaceId: logs.id
    logs: [{ categoryGroup: 'allLogs', enabled: true }]
  }
}

// ---------------------------------------------------------- role assignments

// Gateway -> model: the only identity allowed to call the model directly.
resource apimModelUser 'Microsoft.Authorization/roleAssignments@2022-04-01' = {
  name: guid(foundry.id, apim.id, roles.cognitiveServicesOpenAIUser)
  scope: foundry
  properties: {
    principalId: apim.identity.principalId
    principalType: 'ServicePrincipal'
    roleDefinitionId: subscriptionResourceId('Microsoft.Authorization/roleDefinitions', roles.cognitiveServicesOpenAIUser)
  }
}

// Gateway -> Application Insights: send logs and token metrics with Entra auth.
resource apimMetricsPublisher 'Microsoft.Authorization/roleAssignments@2022-04-01' = {
  name: guid(appInsights.id, apim.id, roles.monitoringMetricsPublisher)
  scope: appInsights
  properties: {
    principalId: apim.identity.principalId
    principalType: 'ServicePrincipal'
    roleDefinitionId: subscriptionResourceId('Microsoft.Authorization/roleDefinitions', roles.monitoringMetricsPublisher)
  }
}

// App -> search: read the index, nothing else.
resource appSearchReader 'Microsoft.Authorization/roleAssignments@2022-04-01' = {
  name: guid(search.id, appIdentity.id, roles.searchIndexDataReader)
  scope: search
  properties: {
    principalId: appIdentity.properties.principalId
    principalType: 'ServicePrincipal'
    roleDefinitionId: subscriptionResourceId('Microsoft.Authorization/roleDefinitions', roles.searchIndexDataReader)
  }
}

// Deployer -> search: create the index and load documents (the postprovision hook),
// and read it when running the CLI from a laptop. Remove after the demo.
resource deployerSearchRoles 'Microsoft.Authorization/roleAssignments@2022-04-01' = [
  for role in (empty(principalId) ? [] : [roles.searchServiceContributor, roles.searchIndexDataContributor]): {
    name: guid(search.id, principalId, role)
    scope: search
    properties: {
      principalId: principalId
      principalType: 'User'
      roleDefinitionId: subscriptionResourceId('Microsoft.Authorization/roleDefinitions', role)
    }
  }
]

output searchEndpoint string = 'https://${search.name}.search.windows.net'
output searchIndex string = searchIndexName
output gatewayUrl string = '${apim.properties.gatewayUrl}/openai/v1'
output modelDeployment string = model.name
output appIdentityClientId string = appIdentity.properties.clientId
