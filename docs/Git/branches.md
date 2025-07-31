# Branches

A branch in git is a way to create different versions of your code and keep them
separated.

## Checkout

Checkout is for switching branches: ``git checkout main``

Checkout is also how you can create new branches:
```bash
git checkout -b new_branch
# this is shorthand for
git branch new_branch
git checkout new_branch
```

You can use checkout to do a lot more:
```bash
# pull a file from another branch
git checkout main -- README.md
```


Below are some examples of some reasons to create a branch.

```bash
# create a new branch for a feature
git checkout -b feature/login-form

# create a branch for a bug fix
git checkout -b fix/issue-123-crash

# create a branch for experiments
git checkout -b experiment/redesign

# separate production from development
git checkout -b production
git checkout -b development
```

## Example Workflow
```bash
# make new branch
git checkout -b test_branch

# make change to file

# commit the change.
git commit -m "update message"

# (optional) push to remote
git push
# or
git push origin test_branch

# switch back to main so we can merge the new branch
git checkout main

# make sure main is up-to-date
git pull

# merge the branch into main
git merge test_branch

# you can also delete the branch afterward if you do not expect to use it
git branch -d test_branch

# if it wasn't merged and you still want to delete
git branch -D test_branch

# (optional) clean up the remote
git push origin --delete test_branch
```

Note: when you push to remote, you are only pushing the active branch.
If you want to push all from local to remote: ``git push --all origin`` BE CAREFUL WITH THIS.

