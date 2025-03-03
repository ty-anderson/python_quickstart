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
- ``rsync -avz --rsync-path="sudo rsync" -e "ssh -p 2222" /Users/tyleranderson/Bonus tyler@anderson.home:/home/tyler/backup``
- ``rsync -avz --rsync-path="sudo rsync" /Users/tyleranderson/Bonus tyler@anderson.home:/home/tyler/backup``

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

## Tar Files

A tar file ``.tar`` is an archive file that stores multiple files and 
directories together in one file, without compression. Very common
in Linux and Unix based systems. Common for backups and transfers.

- Create tar file = ``tar -cvf archive.tar /path/to/files/``
- Extract tar file = ``tar -xvf archive.tar``
- Create compressed tar file = ``tar -czvf archive.tar.gz /path/to/files/``
- Extract compressed tar file = ``tar -xzvf archive.tar.gz``
- List files in tar file = ``tar -tvf archive.tar``
- Extract specific file from tar file = ``tar -xvf archive.tar file.txt``

Flags:

- ``-c`` = Crete new archive
- ``-v`` = Verbose mode (shows progress)
- ``-f`` = Specifies filename (archive.tar)
- ``-x`` = Extract
- ``-z`` = Compress with gzip

### Philosophy

Best practice for backing up files is called 3-2-1 backup strategy.

- 3 copies of your data (original and two backups).
- 2 different storage types (external drive, NAS, cloud storage, etc).
- 1 off-site backup, a cloud backup or physical backup at a friends house.

### Encryption

``age`` is a lightweight focused encryption software for files. 
It uses modern cryptography making it more secure, but less featured 
than something like ``gpg``.

Simple example, one file: ``age -o secretfile.age -p secretfile.txt``

Simple example, directory (use tar): 
    - ``tar -czf myfolder.tar.gz myfolder/``
    - ``age -o myfolder.tar.gz.age -p myfolder.tar.gz``

- MacOS Install: ``brew install age``
- Linux Ubuntu Install: ``sudo apt install age``

### Removing Sensitive Data

Hard-Disk Drives:

Securely delete a file with ``shred``. This will overwrite the file with 
random data mutliple times, renames the file multiple times to obscure 
its original name, then deletes the file. This makes it very difficult 
for data recovery tools to extract meaningful information from the files.

``shred -u secret.txt``

- ``-u`` = truncate and delete the file after shredding.
- ``-n`` = number of times to overwrite (defualt is 3) ``shred -n 10 secret.txt``

Solid-State Drives:

1. Use ``fstrim`` (Best for Full SSD)
✅ Best for clearing free space on an SSD

Modern SSDs support TRIM, which tells the SSD to permanently erase deleted data

``sudo fstrim -v /``

2. Use srm or wipe (For File-Level Deletion)
✅ Best for deleting a single file securely (better than ``shred`` on SSDs)

🔹 Install srm (Secure Remove)

```
sudo apt install secure-delete  # Debian/Ubuntu
brew install srm               # macOS
```

🔹 Securely delete a file = ``srm -v my_secret_file.txt`` 

🔹 Use wipe for Directories = ``wipe -rf my_secret_folder/``
