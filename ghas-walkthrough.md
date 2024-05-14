# GHAS Walkthrough

This repository leverages GitHub Advanced Security (GHAS) to demonstrate it's core functionality and features.
Consider the sections below as a simple lab walkthrough of the various features of GHAS, how to find them, and how to enable them.

Items with a green check (✅) are the specific learning objectives for this walkthrough. If you are comfortable with all these items, you should have a good understanding of how to work with GHAS in an effective manner.

> If you haven't run secrets scanning, CodeQL or other SAST tools on your code base, it's highly likely you will get a flood of alerts. While this is normal, its crucial your organization has a plan to address existing technical debt before enabling security scanning features at scale.

## Table of Contents

- [Setting up GHAS on this repository](#setting-up-ghas-on-this-repository)
- [Secrets Scanning](#secrets-scanning)
    - [Secrets Push Protection](#secrets-push-protection)
    - [Custom Secret Patterns](#custom-secret-patterns)
- [Code Scanning with CodeQL](#code-scanning-with-codeql)
- [Triage Code Scanning Alerts](#triage-code-scanning-alerts)
- [Dependabot](#dependabot)
    - [Enabling Dependabot](#enabling-dependabot)
    - [Enabling Dependabot Version Updates](#enabling-dependabot-version-updates)
- [Third Party Code Scanning](#third-party-code-scanning)
    - [Trivy IaC Scanning](#trivy-iac-scanning)
    - [Dependency Review (by GitHub)](#dependency-review-by-github)
- [Re-usable Workflows](#re-usable-workflows)
- [Security Overview (Reporting)](#security-overview-reporting)
- [Security Manager Role](#security-manager-role)

# Setting up GHAS on this repository

In order to run through the features, simply fork this repository and enable the features you want to test. For quick testing you can fork this on your personal account and keep the visibility public. Most GHAS features are free for public repositories.

> All subsequent sections assume you have following these steps:

1. Fork the repository. 
2. In your fork, go to **Settings** > **Code Security & analysis** and enable _all_ the security features.

**References**:

* [Managing security and analysis settings for your repository](https://docs.github.com/en/enterprise-cloud@latest/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-security-and-analysis-settings-for-your-repository)
* [Quick start for securing your repository](https://docs.github.com/en/enterprise-cloud@latest/code-security/getting-started/quickstart-for-securing-your-repository)
* [Managing security an analysis settings for your organization](https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-security-and-analysis-settings-for-your-organization)

- ✅ Walkthrough repository level GHAS settings.
- ✅ Walkthrough organization level GHAS settings.

# Secrets Scanning

Review the secret scanning alerts for this repository under **Security** > **Secret Scanning**. There are not going to be many secrets identified because the precision of GitHub Secrets scanning is very high (false positives are minimized compared to other scanning solutions like TruffleHog or GitLeaks).

Take a look at the Support Secret provider patterns table under [Supported Secrets](https://docs.github.com/en/code-security/secret-scanning/secret-scanning-patterns#supported-secrets). Here you can see which secret providers are supported by GitHub and which, which are reported to partners, and which are supported for Push Protection.

There's another feature in beta called [Generic Secrets Detection](https://docs.github.com/en/code-security/secret-scanning/secret-scanning-patterns#supported-secrets). This leverages AI to scan and create alerts for unstructured secrets, such as passwords. The false positive rate is likely to be higher for this feature.

Look for Active secrets first. When prioritizing found secrets, use the **Validity** filter set to **Active** to show secrets that are know to be valid.

You can [exclude directories from secret scanning for users](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/configuring-secret-scanning-for-your-repositories) by creating a [`.github/secret-scanning.yml`](./.github/secret_scanning.yml) file in the repository. 

- ✅ Review existing secret alerts. Find alerts that have a validity of Active.
- ✅ Review the supported secret providers and the partner checking for secrets.
- ✅ Be sure to understand when you need to use [`.github/secret-scanning.yml`](./.github/secret_scanning.yml).

## Secrets Push Protection

Secrets Push protection will review developer commits and prevent any pushes on commits that contain secrets. When you consider the high default precision and partner checking for secrets, this is an incredibly powerful feature. Consider the time it takes to block a developer to make a decision on a secret push versus the time it takes to remediate a secret leak.

For more information, see push [protection for repositories and organizations](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/push-protection-for-repositories-and-organizations). 

I typically recommend enabling this feature for all repositories with an org-level settings.

- ✅ Understand how to enable secrets push protection for a repository or and organization.

## Custom Secret Patterns

If you have patterns that are not supported by GitHub, for example an RSA Private Key, you can [define a custom secret scanning pattern](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning). 

> This feature is not enabled for public repositories.

You can set this at the repository level, or preferably the organization level under your organization's **Settings** >  **Code Security** > **Global Settings** > **Custom patterns**. 

For example, say you wanted to ensure that RSA private keys get scanned. You could add the following pattern:

```yaml
-----BEGIN RSA PRIVATE KEY-----[\s\S]*?-----END RSA PRIVATE KEY-----
```

You can then both test the pattern with a test string as well as perform a dry run across your entire organization.

> You need to enable Push Protection for each individual custom pattern!

- ✅ Make sure you can define a custom secret pattern at the organization level.
- ✅ You should be able to test the pattern as well as perform a dry run across your organization before publishing the pattern.

# Code Scanning with CodeQL

There are two ways to set up CodeQL:

* [The default setup](https://docs.github.com/en/enterprise-cloud@latest/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning) - This allows you to set up code scanning at scale and will allow GitHub to find the optimal configuration for your repository. You can also [enable the default set up at scale](https://docs.github.com/en/enterprise-cloud@latest/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning-at-scale) for you organization. 
* [Configuring the advanced setup for code scanning](https://docs.github.com/en/enterprise-cloud@latest/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/configuring-advanced-setup-for-code-scanning) allow you to configure the CodeQL analysis workflow yourself. You will need to add a `.github/workflows/codeql-analysis.yml` file to each an every repository to enable this. If you do leverage the advanced setup, you will want to be familiar with all the topics found under [customizing your advanced setup for code scanning](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/customizing-your-advanced-setup-for-code-scanning#defining-the-severities-causing-pull-request-check-failure). 

See [codeql-config.yml](./.github/workflows/codeql.yml) for an example of a CodeQL configuration file in this repository.

> Leveraging a [reusable workflow](https://docs.github.com/en/actions/using-workflows/reusing-workflows) is a good way to enable CodeQL at scale if you do want to use the advanced setup. For an example of what a reusable workflow looks like for CodeQL, see https://github.com/actions/reusable-workflows/blob/main/.github/workflows/codeql-analysis.yml. This will allow you to keep the workflow configuration managed in a single location.

> GitHub does not support creating CodeQL configuration files dynamically. There is a project called [evergreen](https://github.com/github/evergreen) that is going in that direction, but keeping custom yaml configurations up-to-date is still a manual process or requires custom tooling.

- ✅ Be sure to understand the tradeoffs between the default setup and advanced setup for CodeQL.
- ✅ Understand the language support for CodeQL.
- ✅ Review the [codeql-config.yml](./.github/workflows/codeql.yml) file in this repository. Review the difference between the Python and Java configurations. Be sure you understand when the action is run.
- ✅ Can you identify the historical CodeQL runs and how long they took?

# Blocking Pull Requests with Code Scanning Alerts

When you are [triaging code scanning alerts in pull requests](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/triaging-code-scanning-alerts-in-pull-requests), you can block pull requests on [code scanning check failures](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/triaging-code-scanning-alerts-in-pull-requests#code-scanning-results-check-failures). You will typically only block on critical/high alerts to eliminate too much noise in the developer workflow.

> Only code that has changed as part of a pull request and has a referenced file in the repository and line number will be used in pull request checks.

- ✅ Understand how to block PRs on Code Scanning alerts. Make sure your branch protection rules are set up to block PRs on failed status checks.
- ✅ We'll walk through some pull requests to show what it looks like.

# Triage Code Scanning Alerts

Aside from CodeQL, any tools that run as a GitHub action and scan code [can contribute](https://docs.github.com/en/code-security/code-scanning/integrating-with-code-scanning/sarif-support-for-code-scanning) to Code Scanning alerts in a repository. You can [manage code scanning alerts at the repository](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/managing-code-scanning-alerts-for-your-repository).

There are multiple options for filtering, dismissing, reviewing, and fixing alerts. The quality of the documentation in the alert will depend on the specific alert and the tool that generated it. Be sure to look for suggested remediation steps, related CWEs and well as the sources and skinks for the source code.

- ✅ Be sure your existing policy can map properly to the triage process. If you don't have a policy or it does not work with the GHAS workflows, you may need to adjust your policy.

# Dependabot

Dependabot is a vulnerability scanning and dependency update tool that runs outside the normal commit and pull request cycle. While Dependabot will create alerts for vulnerabilities, it will not block commits or pull requests like Code Scanning or Secrets Push Protection.

> If you want additional protection of blocking PRs on vulnerabilities or disallowed licenses, see the Dependency Review section below.

## Enabling Dependabot

You can enable Dependabot at the repository level under **Settings** > **Security & Analysis** > **Code Scanning** > **Dependabot alerts**. You can also enable Dependabot at the organization level under **Settings** > **Security & Analysis** > **Code Scanning** > **Dependabot alerts**.

If you are new to Dependabot, I suggest reading the [Dependabot Quickstart Guide](https://docs.github.com/en/code-security/getting-started/dependabot-quickstart-guide).

## Enabling Dependabot Version Updates

In order to [configure Dependabot version updates](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/configuring-dependabot-version-updates) you will need to create a `.github/dependabot.yml` file in the repository. This file will allow you to configure the version updates for your dependencies. For an example of `pip` and `maven` package manager checks see the [dependabot.yml](./.github/dependabot.yml) file in this repository.

See also [About dependabot version updates](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/about-dependabot-version-updates) for ecosystem support details.

- ✅ Review the [dependabot.yml](./.github/dependabot.yml) file in this repository. Be sure to understand how package managers are added and where to find the pull requests for version updates.

## Dependabot Features

* [Dependabot alerts](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/about-dependabot-alerts) - Review the documentation for Dependabot Alerts and frequency of pull requests.
* **Dependency Graph** - The [dependency graph](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/about-the-dependency-graph) has 3 main components for viewing your dependencies:
    * **[Dependencies view](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/exploring-the-dependencies-of-a-repository#dependencies-view)** - This shows you all the currently found dependencies and known licenses.
    * **[Dependents View](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/exploring-the-dependencies-of-a-repository#dependents-view)** - Shows you how the repository is being used my other repositories.
    * **Dependabot** - This view show you the specific package managers being scanned and details on recent job updates. 

> NOTE: The reported licenses are only as good as the package repositories are that report this. It very common for licenses to be misreported or not reported at all.

- ✅ Walkthrough the Insights > Dependency Graph for this repository. Do you understand the difference between the Dependencies, Dependents and Dependabot views?

# Third Party Code Scanning

The [GitHub marketplace](https://github.com/marketplace) has thousands of third-party actions that can be explored to augment your development and security workflows. You can [filter on the security category](https://github.com/marketplace?category=security&copilot_app=false&query=&type=&verification=) to explore tools that you might already be using that you can integrate into your existing workflow.

The following sections are tools that I've found useful and are demoed as part of this repository.

- ✅ Review the [GitHub Marketplace](https://github.com/marketplace).

## Trivy IaC Scanning

An example of scanning Terraform is provided in the [trivy-config.yml](./.github/workflows/trivy-config.yml) file. This workflow will scan the Terraform code in the repository for vulnerabilities.

The [Trivy Action](https://github.com/aquasecurity/trivy-action) can be configured to scan IaC files as well as Docker images for OS-level library vulnerabilities.

- ✅ Review the [trivy-config.yml](./.github/workflows/trivy-config.yml) file.
- ✅ Create a branch and modify [main.tf](./iac-misconfiguration/main.tf) to review the alerts generated by Trivy in a PR.
- ✅ Review existing alerts in the Security tab for the repository.

## Container Scanning

> This is not currently covered. But it's important to know that Dependabot does not support scanning of OS-level dependencies. For that you will need to scan the container image itself during the build process, the container registry, and/or the live container in production.

## Dependency Review (by GitHub)

The [dependency review action](https://github.com/actions/dependency-review-action) allows you to scan changed manifest files for dependencies with vulnerabilities, forbidden packages, and forbidden licenses.

This can be useful if you want to be able to block PRs for critical issues. This can be a good shift-left solution where Dependabot won't block existing vulnerabilities from being merged.

Additionally, this is the only solution I'm aware of that will reasonably block known OSS licenses. This can be useful if you have a policy that requires certain licenses to be used in your code base.

- ✅ Checkout the dependency review action in the [dependency-review.yml](./.github/workflows/dependency-review.yml) file.
- ✅ When a package manager file has changed in a PR, can you see the PR comments and the Action step report?

# Security Overview (Reporting)

The [security overview documentation](https://docs.github.com/en/enterprise-cloud@latest/code-security/security-overview/about-security-overview) contains details on what you can do from a Security (GHAS) reporting standpoint at the organization and enterprise levels. Overview reporting is not available at the repository level.

- ✅ Walk through the Security Overview for an Enterprise and Organization. Be sure to understand the difference between the two.
- ✅ Consider what questions you have and what insights you want your security program to generate. Some will be answerable in the reporting, some you will need to build custom reports for.

> NOTE: A common limitation of reporting is the ability to identify alerts that are out of SLA. This is a common example where custom reporting may be necessary.

# Security Manager Role

If you just want to allow individuals access to all Security reporting and settings, be sure to review [Managing security managers in your organization](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization).

- ✅ Be sure you understand what this role is for an if you need to consider it for your enterprise or organization.

# Defense In Depth

A final note on DevSecOps. In order to build a defense-in-depth strategy, I recommend following the guidance of [Cloud Security Alliance's](https://cloudsecurityalliance.org/) [Six Pillars of DevSecOps](https://cloudsecurityalliance.org/blog/2021/09/09/six-pillars-of-devsecops-series). When choosing a scanning solution, it's important to consider how it fits into your overall security strategy. 

For a quick reference, here's a picture of the [Six Pillars of DevSecOps](https://github.com/austimkelly/blog/blob/main/excalidraw/six-pillars-devsecops/six-pillars-reference.png).

This design is also provided [as an Excalidraw file](https://github.com/austimkelly/blog/tree/main/excalidraw/six-pillars-devsecops) if you wanted to leverage this for your own purposes.