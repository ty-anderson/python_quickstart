# Linux

## Execute files

To execute file: ``. path/to/file`` or ``source path/to/file``

Example: ``. bash_script.sh`` or ``source bash_script.sh``

## File Permissions

How to check file permissions: 

- ``ls -l`` - view permissions of files in the directory.
- ``ls -ld`` - view permissions of the directory itself.

drwxr-xr-x  2 root root 4096 Feb 12 12:34 /srv/web_apps

- The first column (drwxr-xr-x) shows the permissions.
  - ``d`` -> directory.
  - ``rwx`` -> Owner: read, write, execute
  - ``r-xr`` -> Group: read, execute, no write
  - ``r-x`` -> Others: read, execute, no write.
- The third column (e.g., ``root root``) shows the owner and group.


``whoami`` - find the user logged in.
``groups`` - show the groups you are in.

You can run commands via ssh

``ssh user@server "ls -ld /srv/web_apps"``

| Section | Meaning                          | Who it applies to      |
|---------|----------------------------------|------------------------|
| d       | Directory                        | -                      |
| rwx     | read(r), write(w), execute(x)    | Owner (root)           |
| r-x     | read(r), no write(-), execute(x) | Group (root)           |          
| r-x     | read(r), no write(-), execute(x) | Others (everyone else) |

To see if you're root do: ``whoami``. If the output is 'root' then you can write.
If your user is not root, check if your in the root group ``groups``. If your
not in 'root' group, you cannot write.

### Alter Permissions

Use ``chmod``:

Each permission type has a number:

- 4 → Read (``r``)
- 2 → Write (``w``)
- 1 → Execute (``x``)

Combine them:

- 7 (4+2+1) → Read, Write, Execute (``rwx``)
- 6 (4+2) → Read, Write (``rw-``)
- 5 (4+1) → Read, Execute (``r-x``)

Example: ``chmod 755 filename``

- Owner: ``rwx`` (7)
- Group: ``r-x`` (5)
- Others: ``r-x`` (5)

Change ownership: ``sudo chown -R user:user /srv/web_apps``

## Copy Directory

Two baked-in commands are ``scp`` or ``rsync``.

Here's an example with scp: ``scp -r ./site user@server:/srv/web_apps``.

rsync is typically recommended over scp.

Copy directory into another:``rsync -av ./site user@server:/srv/web_apps/notes``

Copy directory contents into another:``rsync -av ./site/ user@server:/srv/web_apps/notes/`` (trailing ``/``)


