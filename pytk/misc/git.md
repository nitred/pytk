# Notes

#### How to undo previous commit: [link](http://stackoverflow.com/questions/927358/how-to-undo-last-commits-in-git)
```
# revert the last commit and keeps the changes intact.
git reset --soft HEAD~
# undo git reset
git reset HEAD@{1}
```

#### Git Tags

1. List git tags  
`git tag`

1. Create tag (annotated)  
`git tag -a v1.4 -m "my version 1.4"`

1. Ignore filemode changes from diff
`git config core.fileMode false`
