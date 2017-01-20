### Conda envrionment pip package from git

```
- pip:
  - git+ssh://git@bitbucket.org/user/repo.git#egg=repo
```

### Pip requirements.txt package from git
```
git+ssh://git@bitbucket.org/recogizer/pyrecolog#egg=pyrecolog
```
- apparently the `git@` seems to be required for `git+ssh`
