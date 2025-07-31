# Git Basics

Git is a code repository and version control system. It's great for tracking
changes to a code base (or any other text based files).

There are many tools that can help with basic git functions. The power really
comes from using it in the terminal.

Common commands:
```bash
# start a git project in working directory.
git init

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
Its usually ``.git``. This is a **directory** not a file. Remotes will have similar
naming like python_quickstart.git. 