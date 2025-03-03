# Linux

## Execute files

To execute file: ``./path/to/file`` or ``source /path/to/file``

Example: ``./bash_script.sh`` or ``source /bash_script.sh``

- ``./bash_script.sh`` executes the script as a standalone process. This method requires execute permissions.
- ``source bash_script.sh`` executes the script in the existing process (doesn't create standalone process). Allows
modifying environment variables in the current shell. Allows ``cd`` command to change directory.

TLDR: default to using ``source`` to execute files.

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

Use ``chmod``

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

### Change Ownership

Change the owner of the file to a different user: ``sudo chown -R user:user /srv/web_apps``

## Copy Directory

Two baked-in commands are ``scp`` or ``rsync``.

Here's an example with scp: ``scp -r ./site user@server:/srv/web_apps``.

**rsync is typically recommended over scp.**

Rsync usually comes on Linux and MacOS. 

Commands: 

- Basic = ``rsync -v /source/file/name.txt /dest/file``
- Use literal string (preserve string for special characters) = ``rsync -v '/source/file/na$me.txt' /dest/file``
- Send multiple files = ``rsync -v /source/file1.txt /source/file2.txt '/dest'``
- Send over SSH = ``rsync -av /source/file/name.txt user@server:/dest/file``
- Send over SSH with custom port ``rsync -avz -e "ssh -p 2222" /source/file/name.txt user@server:/dest/file``
- Send over SSH with sudo command = ``rsync -v --rsync-path="sudo rsync" yt_download_image.tar user@server:/srv/flask_yt_download``
- Send over entire directory = ``rsync -avz /source/dir /dest/dir``
- Send all files in directory = ``rsync -avz /source/dir/ /dest/dir``

Flags: 

- ``-v`` = verbose mode.
- ``-a`` = archive mode. saves permissions and timestamps.
- ``-z`` = compress files to transfer, lossless compression.
- ``-e`` = execute specific command.
- ``--progress`` = show transfer progress.
- ``--delete`` = remove files from the backup if they were removed from the source.
- ``--exclude`` = Exclude specific files like ``--exclude='*.log' --exclude='/cache/'``

Copy directory into another:``rsync -av ./site user@server:/srv/web_apps/notes``

Copy directory contents into another:``rsync -av ./site/ user@server:/srv/web_apps/notes/`` 
(trailing ``/`` on the source. Trailing source on the destination doesn't matter)

## Backups

Options: Backup files/folders OR full system backup.

Backup folders: daily ``rsync`` to a separate disk
Full system: weekly ``dd`` or ``timeshift``

Can setup with cron to run regularly.
