# Git Basics

Git is a code repository and version control system. It's great for tracking
changes to a code base (or any other text based files).

There are many tools that can help with basic git functions. The power really
comes from using it in the terminal.

## Common Commands
```bash
# start a git project in working directory.
git init

# add a file to git.
git add main.py

# add all files in the directory to git.
git add .

# commit your changes.
git commit -m "Write a message here"

# send your commited git changes to your active remote.
git push

# retrieve commited changes from remote that are not in your local repo.
git pull

# remove all uncommited changes (USE WITH CAUTION, NO RECOVERY OPTIONS)
git reset --hard

```

The location of the git files is a directory in the root directory of your project.
Its usually ``.git``. This is a **directory not a file**. Remotes will have similar
naming like python_quickstart.git. 


## HEAD

HEAD in git is a pointer to which branch and commit you are on. 
Typically, it is on the most recent commit of the selected branch.

## Navigate Old Commits

```bash
git checkout <commit hash>
git checkout HEAD~1     # 1 commit before current HEAD
git checkout HEAD~3     # 3 commits before current HEAD
```

This puts you in a detached HEAD state which means any changes you make wont
be tracked on any branch, they will just float. 

To safely work on an old commit:
```bash
git checkout abc1234        # Go to the commit
git checkout -b fix/legacy-bug   # Create a branch from it
```

What if you want to rollback a commit?

If you haven't pushed to remote:
```bash
# undo commit but keep code changes.
git reset --soft HEAD~1

# completely remove the commit and rollback files to what the last commit was.
git reset --hard HEAD~1 # USE WITH CAUTION
```

To get back to head just checkout the branch:
``git checkout main``
