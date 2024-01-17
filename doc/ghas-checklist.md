# Secrets scanning checklist

* [ ] Enable Secrets Scanning - See [Configure secrets scan](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/configuring-secret-scanning-for-your-repositories)
* [ ] Enabled Secrets Push Protection - See [Push protection for repositories](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/push-protection-for-repositories-and-organizations)
* [ ] Understand the scanning patterns and limitations of secrets scanning and push protection -  See [Push protection limitations](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/troubleshooting-secret-scanning#push-protection-limitations) and [Secret scanning patterns](https://docs.github.com/en/code-security/secret-scanning/secret-scanning-patterns)
* [ ] Find & manage secret alerts - See [Manage secret alerts](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/managing-alerts-from-secret-scanning)
* [ ] Try to push a secret with push protection enabled - See [Using secret as a push protection on the command line](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/push-protection-for-repositories-and-organizations#using-secret-scanning-as-a-push-protection-from-the-command-line)
* [ ] Create a custom secret scanning pattern - [See Define Custom Patterns](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning). This requires an enterprise license.
* [ ] Create an exclude pattern for files and folders - See [Excluding directories from secrets scanning alerts for users](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/configuring-secret-scanning-for-your-repositories#excluding-directories-from-secret-scanning-alerts-for-users)


# Dependabot alerts checklist

* [ ] Enable Dependabot alerts - See [Configuring Dependabot Alerts](https://docs.github.com/en/enterprise-cloud@latest/code-security/dependabot/dependabot-alerts/configuring-dependabot-alerts)
* [ ] Configure Dependabot custom rules - See [Configuration options for the dependabot.yml file](https://docs.github.com/en/enterprise-cloud@latest/code-security/dependabot/dependabot-version-updates/configuration-options-for-the-dependabot.yml-file#configuration-options-for-the-dependabotyml-file)
    - [ ] Review options for version updates - See [Version updates example](https://docs.github.com/en/enterprise-cloud@latest/code-security/dependabot/dependabot-version-updates/configuring-dependabot-version-updates#example-dependabotyml-file)
    - [ ] Review options for security updates - See [Security updates example](https://docs.github.com/en/enterprise-cloud@latest/code-security/dependabot/dependabot-security-updates/configuring-dependabot-security-updates#example-dependabotyml-file)
* [ ] Enable Dependabot Security Updates - See [Configuring dependabot security updates example](https://docs.github.com/en/enterprise-cloud@latest/code-security/dependabot/dependabot-version-updates/configuring-dependabot-version-updates#example-dependabotyml-file)
* [ ] Enable Dependabot Grouped Security Updates (Beta) - See [Configuring Dependabot Grouped Security Updates](https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/configuring-dependabot-security-updates#grouping-dependabot-security-updates-into-a-single-pull-request)
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
* [ ] Review the CodeQL workflow file
    * [ ] Open [codeql.yml](../.github/workflows/codeql.yml)
    * [ ] What branches are scanned? - See [Avoiding unnecessary scans of pull requests](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/customizing-your-advanced-setup-for-code-scanning#avoiding-unnecessary-scans-of-pull-requests)
    * [ ] What languages are scanned? - See [Changing the languages that are analyzed](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/customizing-your-advanced-setup-for-code-scanning#changing-the-languages-that-are-analyzed)
    * [ ] What is `autobuild` for in CodeQL? - See [CodeQL for compiled languages](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages)
    * [ ] How often is a full scan performed? - See [Scanning on a schedule](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/customizing-your-advanced-setup-for-code-scanning#scanning-on-a-schedule)
    * Review query packs used - See [Using queries in QL packs](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/customizing-your-advanced-setup-for-code-scanning#using-queries-in-ql-packs)
    * Review how to specify directories to scan - See [Specifying directories to scan](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/customizing-your-advanced-setup-for-code-scanning#specifying-directories-to-scan)
* [ ] Review 3rd party code scanning workflows
    * [ ] Check out the [tfsec](../.github/workflows/tfsec.yml) workflow (aka defsec)
    * [ ] Review the other 3rd party workflows you can add
* [ ] Review Code scanning alerts list
    - [ ] Review search facets and filters - See [Managing code scanning alerts for your repository](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/managing-code-scanning-alerts-for-your-repository)
* - Review a single alert - See [Managing alerts](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/managing-code-scanning-alerts-for-your-repository)
    - [ ] Review severity
    - [ ] Review related CVE/CWEs
    - [ ] Review the source of the CodeQL query
    - [ ] Review sources and sink (Show Paths) - Note, not all alerts will have Show Paths.
    - [ ] Follow the sink to the code line(s) and see the Copilot X icon. Can you get advice on how to fix it?
    - [ ] Note the dismissal options for a Code scanning alert - See [Dismissing code scanning alerts](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/triaging-code-scanning-alerts-in-pull-requests#dismissing-an-alert-on-your-pull-request)
    - [ ] Review summary, descriptions, fixes and references
    - [ ] Review commit history

# Security advisories

* [ ] Create a security advisory - See [About Security Advisory](https://docs.github.com/en/enterprise-cloud@latest/code-security/security-advisories/working-with-repository-security-advisories/about-repository-security-advisories)

# Security policy

* [ ] Review the security policy - See [Adding a security policy to your repository](https://docs.github.com/en/enterprise-cloud@latest/code-security/getting-started/adding-a-security-policy-to-your-repository)

# General

* [ ] Review branch protection rules - See [Managing a branch protection rule](https://docs.github.com/en/enterprise-cloud@latest/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/managing-a-branch-protection-rule)
* [ ] Review repository permissions - [Managing your repositories teams and people](https://docs.github.com/en/enterprise-cloud@latest/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/managing-teams-and-people-with-access-to-your-repository)
* [ ] Review Security Overview (Requires Owner or Admin permission on the Org) - See [About the security overview](https://docs.github.com/en/enterprise-cloud@latest/code-security/security-overview/about-security-overview)
* [ ] Review API for pull GHAS repo info - See [Code Scanning API](https://docs.github.com/en/enterprise-cloud@latest/rest/reference/code-scanning). See also https://github.com/austimkelly/ghas-utils for org-level insights across multiple repos. 
* [ ] Github Action using REST API. There is an action in this repository you can run if you have a personal access token. It will check to see you have all the core GHAS features enabled on the repository. See also [check-ghas-features.yml](../.github/workflows/check-ghas-features.yml) for how to make REST API calls via a Github action.