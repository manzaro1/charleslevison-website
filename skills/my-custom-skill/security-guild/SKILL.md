# Security Guild Skill

A comprehensive security hardening and best practices skill for OpenClaw deployments.

## Overview

This skill provides security auditing, GitHub security, and deployment hardening for your workspace. It implements a defense-in-depth approach following industry best practices.

## Features

### 1. GitHub Security
- **Secret Scanning**: Detect API keys, tokens, passwords in commits
- **Branch Protection**: Enforce PR requirements
- **Commit Verification**: GPG signed commits

### 2. Local Git Workflow
- **Pre-commit Hooks**: Block secrets before push
- **Gitea Support**: Self-hosted Git option
- **CI Pipeline**: Security scanning before deploy

### 3. Deployment Security
- **Network Segmentation**: Isolate sensitive services
- **Container Audits**: Check for vulnerabilities
- **Access Control**: Principle of least privilege

### 4. Agent Constraints
- **Read-only by Default**: Only write when needed
- **Audit Logging**: All actions logged
- **Branch Protection**: Cannot override main

## Commands

### Security Audit
```bash
openclaw security audit
```
Run full security audit of the workspace.

### Check for Secrets
```bash
openclaw security scan-secrets
```
Scan repository for hardcoded secrets.

### Enable Branch Protection
```bash
openclaw security branch-protection
```
Configure GitHub branch protection rules.

### Generate API Key
```bash
openclaw security generate-key [service]
```
Generate secure API key for specified service.

### Check Container Security
```bash
openclaw security container-scan
```
Scan running containers for vulnerabilities.

## Security Checklist Implementation

### ✅ Pre-push Hooks
- TruffleHog secret scanner
- GitGuardian pre-commit
- Custom regex patterns for common secrets

### ✅ Local-first Git Workflow
- Gitea self-hosted option
- Woodpecker CI integration
- Human review required

### ✅ Defense in Depth
- 1Password vault integration (configurable)
- Network segmentation guides
- Daily automated audits

### ✅ Agent Constraints
- Branch protection enforced
- Read-only access by default
- Full audit logging

## Configuration

Create `~/.openclaw/security.yaml`:

```yaml
github:
  token: your_github_token
  org: your_org
  
gitea:
  url: https://gitea.example.com
  token: your_gitea_token
  
vault:
  provider: 1password
  vault_name: openclaw
  
containers:
  scanner: trivy
  
network:
  segmentation: true
  sensitive_services:
    - database
    - api_keys
```

## Daily Security Tasks

The skill includes automated daily checks:
1. Scan for new secrets in code
2. Check container vulnerabilities
3. Verify branch protection
4. Audit access permissions
5. Generate security report

## Usage Examples

### Running a Security Audit
```bash
openclaw security audit --full
```

### Scanning for Secrets
```bash
openclaw security scan-secrets --fix
```

### Setting Up Branch Protection
```bash
openclaw security branch-protection --repo my-repo
```

## Integration Points

- **GitHub**: Secret scanning, branch protection
- **Gitea**: Self-hosted Git repos
- **1Password**: Secret management
- **Trivy**: Container scanning
- **Woodpecker CI**: Pipeline security

## Troubleshooting

### "Permission denied" errors
- Check GitHub token has correct scopes
- Verify branch protection settings

### Secrets detected
- Use environment variables instead of hardcoded values
- Add secrets to 1Password vault

### Container scan fails
- Ensure Docker is running
- Check Trivy is installed

## Best Practices

1. **Never commit secrets** - Use env vars or vault
2. **Enable 2FA** - On all accounts
3. **Use GPG signing** - For commits
4. **Regular audits** - Run weekly scans
5. **Limit access** - Principle of least privilege

## Support

For issues or questions:
- Check GitHub security alerts
- Review audit logs
- Consult security documentation
