<!-- Place at .github/copilot-instructions.md in the engagement repo -->
# Copilot Instructions

- Follow RPI (HVE Core): no implementation without a plan in `.copilot-tracking/`.
- IaC: Bicep or Terraform using Azure Verified Modules. Managed identity only; never emit keys.
- Agents: Microsoft Agent Framework (Python or .NET). Narrow tool contracts; approval required for write actions.
- Emit OpenTelemetry for every agent and tool call.
- Fabric deployments use `fabric-cicd` with an explicit `token_credential`.
- Mark any dependency on a preview feature with `# PREVIEW:` and a link to its docs.
- Use the Azure MCP Server for Azure context; never grant the Copilot cloud agent more than Reader without an ADR.
- Reference Foundry roles by GUID in IaC (roles were renamed from Azure AI * to Foundry *).
