# Secrets scanning checklist

* [ ] Enable Secrets Scanning - See [Configure secrets scan](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/configuring-secret-scanning-for-your-repositories)
* [ ] Enabled Secrets Push Protection - See [Push protection for repositories](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/push-protection-for-repositories-and-organizations)
* [ ] Find & manage secret alerts - See [Manage secret alerts](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/managing-alerts-from-secret-scanning)
* [ ] Try to push a secret with push protection enabled
* [ ] Create a custom secret scanning pattern - [See Define Custom Patterns](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning)
* [ ] Create an exclude pattern for files and folders - See [Excluding directories from secrets scanning alerts for users](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/configuring-secret-scanning-for-your-repositories#excluding-directories-from-secret-scanning-alerts-for-users)

# Dependabot alerts checklist

* [ ] Enable Dependabot alerts - See [Configuring Dependabot Alerts](https://docs.github.com/en/enterprise-cloud@latest/code-security/dependabot/dependabot-alerts/configuring-dependabot-alerts)
* [ ] Configure Dependabot custom rules
* [ ] Enable Dependabot Security Updates - See [Configuring Dependabot Security Updates](https://docs.github.com/en/enterprise-cloud@latest/code-security/dependabot/dependabot-security-updates/configuring-dependabot-security-updates)
* [ ] Enable Dependabot Grouped Security Updates (Beta)
* [ ] Configure Dependabot version updates - See [Configuring Dependabot version updates](https://docs.github.com/en/enterprise-cloud@latest/code-security/dependabot/dependabot-version-updates/configuring-dependabot-version-updates)
* [ ] Configure Dependabot Notifications - See [Configure notifications for Dependabot alerts](https://docs.github.com/en/enterprise-cloud@latest/code-security/dependabot/dependabot-alerts/configuring-notifications-for-dependabot-alerts)
* [ ] Review the Dependency Graph and export an SBOM - See [Viewing the Dependency Graph](https://docs.github.com/en/enterprise-cloud@latest/code-security/supply-chain-security/understanding-your-software-supply-chain/exploring-the-dependencies-of-a-repository#viewing-the-dependency-graph) and [Export dependencies as SBOM](https://docs.github.com/en/enterprise-cloud@latest/code-security/supply-chain-security/understanding-your-software-supply-chain/exporting-a-software-bill-of-materials-for-your-repository)
* [ ] Review Dependabot alerts and review search facets and filters
* [ ] Review a single alert - See [View Dependabot Alert](https://docs.github.com/en/enterprise-cloud@latest/code-security/dependabot/dependabot-alerts/viewing-and-updating-dependabot-alerts)
    - [ ] Find related CVE and CWEs
    - [ ] See "All affected repositories"
    - [ ] See related alerts
    - [ ]  Navigate to the related pull request (if present)
    - [ ] Note the dismissal options for a Dependabot alert - See [Dismissing Dependabot Alerts](https://docs.github.com/en/enterprise-cloud@latest/code-security/dependabot/dependabot-alerts/viewing-and-updating-dependabot-alerts#dismissing-dependabot-alerts)
* [ ] Merge a pull request from Dependabot - See [Managing pull requests for dependency updates](https://docs.github.com/en/enterprise-cloud@latest/code-security/dependabot/working-with-dependabot/managing-pull-requests-for-dependency-updates)
    - [ ]  Review the `@dependabot` chat ops options - See [Managing Dependabot pull requests with comment commands](https://docs.github.com/en/enterprise-cloud@latest/code-security/dependabot/working-with-dependabot/managing-pull-requests-for-dependency-updates#managing-dependabot-pull-requests-with-comment-commands)


# Code scanning with CodeQL

* [ ] Enable Code scanning - See [Configuring code scanning](https://docs.github.com/en/enterprise-cloud@latest/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning)
* [ ] Review the CodeQL workflow
* [ ] Review 3rd party code scanning workflows
* [ ] Review Code scanning alerts
    - [ ] Review search facets and filters
* - Review a single alert
    - [ ] Review severity
    - [ ] Review related CVE/CWEs
    - [ ] Review the source of the CodeQL query
    - [ ] Review sources and sink (Show Paths) - Note, not all alerts will have Show Paths.
    - [ ] Follow the sink to the code line(s) and see the Copilot X icon. Can you get advice on how to fix it?
    - [ ] Note the dismissal options for a Code scanning alert - See [Dismissing code scanning alerts]()
    - [ ] Review summary, descriptions, fixes and references
    - [ ] Review commit history

# Security advisories

* [ ] Create a security advisory

# Security policy

* [ ] Review the security policy

# General

* - [ ] Review branch protection rules
* - [ ] Review repository permissions
* - [ ] Review Security Overview (Requires Owner or Admin permission on the Org)
* - [ ] Review API for pull GHAS repo info