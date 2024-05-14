# GHAS Walkthrough

This repository leverages GitHub Advanced Security (GHAS) to demonstrate it's core functionality and features.
Consider the sections below as a simple lab walkthrough of the various features of GHAS, how to find them, and how to enable them.

## Table of Contents

>> TODO  

# Setting up GHAS on this repository

In order to run through the features, simply fork this repository and enable the features you want to test. For quick testing you can fork this on your personal account and keep the visibility public. Most GHAS features are free for public repositories.

>> All subsequent sections assume you have following these steps:


1. Fork the repository. 
2. In your fork, go to **Settings** > **Code Security & analysis** and enable _all_ the security features.

**References**:

* [Managing security and analysis settings for your repository](https://docs.github.com/en/enterprise-cloud@latest/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-security-and-analysis-settings-for-your-repository)
* [Quick start for securing your repository](https://docs.github.com/en/enterprise-cloud@latest/code-security/getting-started/quickstart-for-securing-your-repository)
* [Managing security an analysis settings for your organization](https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-security-and-analysis-settings-for-your-organization)

# Secrets Scanning

Review the secret scanning alerts for this repository under **Security** > **Secret Scanning**. There are not going to be many secrets identified because the precision of GitHub Secrets scanning is very high (false positives are minimized compared to other scanning solutions like TruffleHog or GitLeaks).

Take a look at the Support Secret provider patterns table under [Supported Secrets](https://docs.github.com/en/code-security/secret-scanning/secret-scanning-patterns#supported-secrets). Here you can see which secret providers are supported by GitHub and which, which are reported to partners, and which are supported for Push Protection.

There's another feature in beta called [Generic Secrets Detection](https://docs.github.com/en/code-security/secret-scanning/secret-scanning-patterns#supported-secrets). This leverages AI to scan and create alerts for unstructured secrets, such as passwords. The false positive rate is likely to be higher for this feature.

Look for Active secrets first. When prioritizing found secrets, use the **Validity** filter set to **Active** to show secrets that are know to be valid.

You can [exclude directories from secret scanning for users](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/configuring-secret-scanning-for-your-repositories) by creating a [`.github/secret-scanning.yml`](./.github/secret_scanning.yml) file in the repository. 

## Secrets Push Protection

Secrets Push protection will review developer commits and prevent any pushes on commits that contain secrets. When you consider the high default precision and partner checking for secrets, this is an incredibly powerful feature. Consider the time it takes to block a developer to make a decision on a secret push versus the time it takes to remediate a secret leak.

For more information, see push [protection for repositories and organizations](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/push-protection-for-repositories-and-organizations). 

I typically recommend enabling this feature for all repositories with an org-level settings.

# Code Scanning with CodeQL

# Triage Code Scanning Alerts

# Dependabot

## Enabling Dependabot

## Enabling Dependabot Version Updates

# Third Party Code Scanning

## Trivy IaC Scanning

## Dependency Review (by GitHub)

# Re-usable Workflows

# Security Overview (Reporting)

## Enterprise Security Overview

## Organization Security Overview

## Repository Security Overview

