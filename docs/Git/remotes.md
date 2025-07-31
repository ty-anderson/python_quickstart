# Git Remotes

A "remote" in the git environment is another location to 
store a copy of your git project.

GitHub is the most common remote.

```bash
# To see all remotes that are in a project
git remote -v

# to push commited updates to remote
git push
```

You can setup multiple remotes on one git project.

```bash
git remote add <name of remote> <server uri>

# for example:
git remote add origin https://github.com/ty-anderson/python_quickstart.git
git remote add backup ssh://user@yourserver:/srv/git/myproject.git

# when pushing be explicit to which remote
git push <remote name> <branch>
git push origin main
git push backup master
```

## Self Hosted Git Server

If you want to store your git projects on your own server, its pretty simple.

Steps:

On your server:
```bash
mkdir -p /srv/git/myproject.git
cd /srv/git/myproject.git
git init --bare
```

On your local machine:
```bash
git remote add origin ssh://user@yourserver:/srv/git/myproject.git
git push -u origin main
# origin is name of remote, change to whatever you want. 
# main is name of branch, change to whatever branch you want to commit.
# the -u sets this remote as the active one for tracking. 
```

