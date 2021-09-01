[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)


## compare-dotenvs


A simple tool for managing your `.env.example` files.

##### Usage:

```shell
$ compare-dotenvs
```

compare-dotenvs can also be used as pre-commit hook.
Basic configuration:

```yaml
- repo: https://github.com/mateuszgrzyb/compare-dotenvs
  rev: master
  hooks:
    - id: compare-dotenvs
```
