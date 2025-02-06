# Contributing

[fork]: https://github.com/IBM/risk-atlas-nexus/fork
[pr]: https://github.com/IBM/risk-atlas-nexus/compare
[released]: https://help.github.com/articles/github-terms-of-service/

We are pleased that you would like to contribute to Risk Atlas Nexus. We welcome both reporting issues and submitting pull requests.

## Reporting issues
Please make sure to include any potentially useful information in the issue, so we can pinpoint the issue faster without going back and forth.

- What SHA of Risk atlas nexus are you running? If this is not the latest SHA on the main branch, please try if the problem persists with the latest version.
- Python versions 
- TBC

## Contributing a change
Contributions to this project are [released][released] to the public under the project's [opensource license](LICENSE.md).

Contributors must _sign off_ that they adhere to these requirements by adding a `Signed-off-by` line to all commit messages with an email address that matches the commit author:

```
feat: this is my commit message

Signed-off-by: Random J Developer <random@developer.example.org>
```
Formatter: run the black formatter on python changes
`python3.11 -m black .`

## Submitting a pull request

The following is the recommended method for changing code

1. [Fork][fork] and clone the repository
2. If a major change create a new branch: `git checkout -b my-branch-name` Otherwise work in main
3. Make your changes, push to your fork and [submit a pull request][pr] to co-devleopers on your fork
4. Wait for your pull request to be reviewed and merged into the main branch of the fork
5. When changes are ready create a pr for the fork's main branch to merge into the upstream's main branch
