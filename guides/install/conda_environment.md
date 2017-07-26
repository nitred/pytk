## Dev Envrionment YML Template
```
name: project-name
channels:
    - defaults
dependencies:
- python=3.6.1
- pip:
    - git+https://github.com/ansrivas/pylogging.git
```


## Conda envrionment pip package from git

```
- pip:
  - git+ssh://git@bitbucket.org/user/repo.git#egg=repo
```

## Pip requirements.txt package from git
```
git+ssh://git@bitbucket.org/user/repo#egg=repo
```
- apparently the `git@` seems to be required for `git+ssh`
