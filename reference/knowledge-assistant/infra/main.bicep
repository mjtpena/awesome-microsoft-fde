// Entry point for `azd up`. Creates one resource group and everything in it.
// Teaching reference: public endpoints, no private networking (see README).
targetScope = 'subscription'

@minLength(1)
@maxLength(40)
@description('azd environment name; used to name the resource group and resources.')
param environmentName string

@minLength(1)
@description('Region for every resource. The model must be available there with the chosen deployment type.')
param location string

@description('Object ID of the person running azd. Gets index-write access and may call the gateway. Set by azd.')
param principalId string = ''

@description('Model to deploy. Check availability and retirement dates for your region before you deploy.')
param modelName string = 'gpt-4.1-mini'
param modelVersion string = '2025-04-14'

@description('Deployment capacity in thousands of tokens per minute. Keep it small for a demo.')
param modelCapacity int = 10

@description('Per-caller token rate limit enforced by the gateway.')
param tokensPerMinutePerCaller int = 5000

@description('API Management requires a publisher email. It receives service notifications.')
param apimPublisherEmail string = 'platform-team@example.com'

var tags = { 'azd-env-name': environmentName, purpose: 'teaching-reference' }

resource rg 'Microsoft.Resources/resourceGroups@2024-03-01' = {
  name: 'rg-${environmentName}'
  location: location
  tags: tags
}

module resources 'resources.bicep' = {
  name: 'resources'
  scope: rg
  params: {
    location: location
    tags: tags
    principalId: principalId
    modelName: modelName
    modelVersion: modelVersion
    modelCapacity: modelCapacity
    tokensPerMinutePerCaller: tokensPerMinutePerCaller
    apimPublisherEmail: apimPublisherEmail
  }
}

// azd stores these in the environment; the CLI and the postprovision hook read them.
output AZURE_RESOURCE_GROUP string = rg.name
output AZURE_SEARCH_ENDPOINT string = resources.outputs.searchEndpoint
output AZURE_SEARCH_INDEX string = resources.outputs.searchIndex
output HARBOURLINE_GATEWAY_URL string = resources.outputs.gatewayUrl
output HARBOURLINE_MODEL string = resources.outputs.modelDeployment
output AZURE_APP_IDENTITY_CLIENT_ID string = resources.outputs.appIdentityClientId
