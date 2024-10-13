# Run GitHub Actions Tests

This document shows the procedure for GitHub Actions debug and test in local docker.

## Pre-requirement

### Docker in Docker

A docker container must be able to mount `/var/run/docker.sock`
to run GitHub Actions inside docker.
So only tested in Linux environment.

### GitHub personal access token

A GitHub personal access token may be required to run workflows.
Which must have Public Repositories (read-only) access.

See: [Managing your personal access tokens - GitHub Docs](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)

## Run GitHub Actions

You can run GitHub Actions using the following commands:
<!-- markdownlint-disable MD013 -->
* Fast (set_versions) test
  * `bash tools/github_actions_tests/run_github_actions_tests.sh --job set_versions`
* List jobs
  * `bash tools/github_actions_tests/run_github_actions_tests.sh --list`
* Lint
  * `bash tools/github_actions_tests/run_github_actions_tests.sh --workflows .github/workflows/lint.yml push`
* Latest bulid test
  * For fake-bpy-module: `bash tools/github_actions_tests/run_github_actions_tests.sh --workflows .github/workflows/fake-bpy-module-latest-build.yml --job build_modules`
  * For fake-bge-module: `bash tools/github_actions_tests/run_github_actions_tests.sh --workflows .github/workflows/fake-bge-module-latest-build.yml --job build_modules`
* All push test
  * `bash tools/github_actions_tests/run_github_actions_tests.sh push`
* Show help
  * `bash tools/github_actions_tests/run_github_actions_tests.sh --help`
  * Detailed command examples: <https://github.com/nektos/act#example-commands>
<!-- markdownlint-disable MD013 -->
