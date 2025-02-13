# Linux

## Execute files

To execute file: ``. path/to/file`` or ``source path/to/file``

Example: ``. bash_script.sh`` or ``source bash_script.sh``

## File Permissions

How to check file permissions: 

- ``ls -l`` - view permissions of files in the directory.
- ``ls -ld`` - view permissions of the directory itself.

You will see something like below:

``drwxr-xr-x  2 root root 4096 Feb 12 12:34 /srv/web_apps``

The first section is read, write, execute for owner, group, others. 

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

There are 2 main methods, numeric or symbolic. The numeric mode requires memorizing number codes for altering permissions.
Symbolic is more straight forward.

- ``u+rwx`` → Add read, write, execute for owner (``u``).
- ``g+r`` → Add read for group (``g``).
- ``o-r`` → Remove read for others (``o``).

Examples:

- Change all permissions: ``chmod u+rwx,g+r,o-r filename``
- Change only owner permissions: ``chmod u+rwx filename``
- Change only group permissions: ``chmod g-w filename``
- Change only other permissions: ``chmod o-r filename``
- Give everyone execute permissions: ``chmod +x filename``



### Change ownership: 

Change the owner of the file to a different user: ``sudo chown -R user:user /srv/web_apps``

## Copy Directory

Two baked-in commands are ``scp`` or ``rsync``.

Here's an example with scp: ``scp -r ./site user@server:/srv/web_apps``.

rsync is typically recommended over scp.

Copy directory into another:``rsync -av ./site user@server:/srv/web_apps/notes``

Copy directory contents into another:``rsync -av ./site/ user@server:/srv/web_apps/notes/`` (trailing ``/``)


