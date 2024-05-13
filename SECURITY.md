# Security Policy

This repository contains simple vulnerabilities based on OWASP Top 10 to teach software developers how to identify security vulnerabilities, used GitHub Advanced Security, and ultimately fix them.

## Supported Versions

Not applicable

## Reporting a Vulnerability

There's no need to report a vulnerability. This code is only meant to run local host for quick atomic exploration of security vulnerabilities.

Typically this is where you suggest how to log vulnerabilities and contact the security team for more questions.

## Security Best Practices

To enhance the security of our project, we have the following requirements:

### Dependabot

We require that Dependabot is enabled for all repositories. Dependabot helps automatically keep your dependencies up-to-date by creating pull requests for outdated dependencies.

#### Enable Dependabot

To enable Dependabot, please follow these steps:

1. Go to the "Security" tab in your repository.
2. Select "Dependabot" from the left navigation.
3. Enable Dependabot for the desired package ecosystems.

### Secrets Push Protection

Secrets Push Protection must be enabled to prevent accidental disclosure of sensitive information in your code.

#### Enable Secrets Push Protection

To enable Secrets Push Protection, please follow these steps:

1. Go to the "Settings" tab in your repository.
2. Select "Secrets" from the left navigation.
3. Enable Secrets Push Protection for your repository.

### CodeQL Analysis

CodeQL must be enabled, blocking merges on Critical and High severity issues. This ensures that critical and high-risk vulnerabilities are addressed before merging changes.

#### Enable CodeQL Analysis

To enable CodeQL Analysis, please follow these steps:

1. Go to the "Security" tab in your repository.
2. Select "Code scanning" from the left navigation.
3. Enable CodeQL Analysis and configure it to block merges on Critical and High severity issues.

Thank you for contributing to the security of our project.

