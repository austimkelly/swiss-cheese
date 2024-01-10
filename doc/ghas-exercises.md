# Summary

This repository massages most of the Github Advanced Security (GHAS) features into a single repository: 

* Dependabot alerts
* Secrets scanning, 
* Code scanning with CodeQL
* Security advisories
* Security policy

When you fork a repository, all GHAS features are disabled by default. Hence, this repo serves as a good way to toggle most of the features of GHAS yourself and walk through some of the existing configurations.

# Goals

You should get core security configuration of the main features of Github Advanced Security. You be able to configure all scanning features and understand basic configuration options, code scanning actions, and YAML config options. 

You should be able to see security alerts and be able to triage and respond to them.

# Requirements

If you fork this repository in a public account, you will have access to all the features in this exercise. GHAS is free on public accounts. See also [GHAS pricing](https://docs.github.com/en/enterprise-cloud@latest/billing/managing-billing-for-github-advanced-security/about-billing-for-github-advanced-security)

# Set-up

1. Fork this repository to your own account.
2. Navigate to `https[X]://github.com/{your account id}/swiss-cheese/settings/security_analysis`. You will see the unset security settings:

![GHAS Settings](./img/empty_security_settings.png)

# Configure the settings

**TODO** This section will need specific tasks and configurations to review. Additional references to Github docs as well.

1. Create security policy

    * TODO

2. Enable Dependabot alerts

    * TODO

3. Enable Code scanning with CodeQL

    * TODO 

4. Enable secret scanning

    * TODO

5. Create a security advisory

    * TODO 

6. Review 

    * TODO

# Results

If you have the configured everything correctly you should have the same security alerts as the public repository your forked from. The exception is the Security Advisories, where are not copied to a forked repository.

![GHAS Completed Settings](./img/ghas-fully-configured.png)


# References

* [GHAS Developer Training](https://github.com/services/ghas-developer-training) - An outline of the core concepts suggested by GitHub.