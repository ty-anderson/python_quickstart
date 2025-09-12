# Backups

Options: Backup files/folders OR full system backup.

Backup folders: daily ``rsync`` to a separate disk
Full system: weekly ``dd`` or ``timeshift``

Can setup with cron to run regularly.

## Philosophy

Best practice for backing up files is called 3-2-1 backup strategy.

- 3 copies of your data (original and two backups).
- 2 different storage types (external drive, NAS, cloud storage, etc).
- 1 off-site backup, a cloud backup or physical backup at a friends house.

## Copy Directory

Two baked-in commands are ``scp`` or ``rsync``.

Here's an example with scp: ``scp -r ./site user@server:/srv/web_apps``.

**rsync is typically recommended over scp.**

``rsync`` usually comes on Linux and MacOS, it is lightweight, fast, can detect
changes in files to do an incremental backup. 

Commands: 

```bash
# Basic save file to another folder
rsync -v /source/file/name.txt /dest/file

# Use literal string (preserve string for special characters)
rsync -v '/source/file/na$me.txt' /dest/file

# Send multiple files
rsync -v /source/file1.txt /source/file2.txt '/dest'

# Send over SSH
rsync -av /source/file/name.txt user@server:/dest/file

# Send over SSH with custom port
rsync -avz -e "ssh -p 2222" /source/file/name.txt user@server:/dest/file

# Send over SSH with sudo command
rsync -v --rsync-path="sudo rsync" yt_download_image.tar user@server:/srv/flask_yt_download

# Send over entire directory
rsync -avz /source/dir /dest/dir

# Send all files in directory. Trailing slash. 
# Trailing slash only matters on source, it doesn't matter on dest
rsync -avz /source/dir/ /dest/dir

# actual use
rsync -avz --rsync-path="sudo rsync" /Users/tyleranderson/PycharmProjects tyler@anderson.home:/srv/backup_media
```

Flags: 

- ``-v`` = verbose mode.
- ``-a`` = archive mode. saves permissions and timestamps.
- ``-z`` = compress files to transfer, lossless compression.
- ``-e`` = execute specific command.
- ``-r`` = copy directories recursively. Meaning all files in subfolders as well.
- ``-h`` = human readable file sizes while coping
- ``--progress`` = show transfer progress.
- ``--delete`` = remove files from the backup if they were removed from the source.
- ``--exclude`` = Exclude specific files like ``--exclude='*.log' --exclude='/cache/'``

## Tar Files

A tar file ``.tar`` is an archive file that stores multiple files and 
directories together in one file, without compression. Very common
in Linux and Unix based systems. Common for backups and transfers.

```bash
# Create tar file (best to use relative path instead of absolute)
sudo tar -cvf archive.tar path/to/files/

# Extract tar file
sudo tar -xvf archive.tar

# Create compressed tar file
tar -czvf archive.tar.gz /path/to/files/

# Extract compressed tar file
tar -xzvf archive.tar.gz

# List files in tar file
tar -tvf archive.tar

# Extract specific file from tar file
tar -xvf archive.tar file.txt
```

Flags:

- ``-c`` = Crete new archive
- ``-v`` = Verbose mode (shows progress)
- ``-f`` = Specifies filename (archive.tar)
- ``-x`` = Extract
- ``-z`` = Compress with gzip

## Encryption

``age`` is a lightweight focused encryption software for files. 
It uses modern cryptography making it more secure, but less featured 
than something like ``gpg``. Age  lets you use passwords or key files.

Install:

```bash
# Install
brew install age  # MacOS
sudo apt install age # Linux
```

How to use - you have 2 options for encryption.

1. Password - best for quick encryption, no need to manage keys. Less secure and harder to automate.

```bash
# encrypt with password, prompt will ask for password
age -o myfile.txt.age -p myfile.txt

# decrypt with password
age -d myfile.txt.age > myfile.txt

```

2. Public/Private key Encryption - Most secure and good for automation.

```bash
# generate a key file
age-keygen -o ~/.age-key.txt  # stores key in ~/.age-key.txt
# This file contains a public and private key that you can use to encrypt files.

# encrypt file using public key (replace PUBLIC_KEY with your public key in the file)
age -r PUBLIC_KEY -o myfile.txt.age myfile.txt

# decrypt using private key
age -d -i ~/.age-key.txt myfile.txt.age > myfile.txt
```

To use the file directly instead of copying the public key:

```bash
# use head to extract the public key
age -r $(head -n 1 ~/.age-key.txt) -o myfile.txt.age myfile.txt

# decrypt
age -d -i ~/.age-key.txt myfile.txt.age > myfile.txt
```

Encrypt directory by turning into tar file, then encrypting that file.

```bash
# Simple example, directory (use tar).
tar -czf myfolder.tar.gz myfolder/
age -o myfolder.tar.gz.age -p myfolder.tar.gz

# convert folder to tar file, encrypt it with age, one command,
# no intermediate file created.
tar -czf - myfolder/ | age -o myfolder.tar.gz.age -p

# decrypt and extract in one command.
age -d myfolder.tar.gz.age | tar -xz
```

Decrypt:

```bash
# decrypt .age file
age -d myfolder.tar.gz.age > myfolder.tar.gz

# extract the file
tar -xzf myfolder.tar.gz

# delete archive file
shred -u myfolder.tar.gz
```

Flags:

- ``-o <output>`` = output file name.
- ``-d`` = decrypts an encrypted file.
- ``-p`` = uses password encryption.
- ``-r <public-key>`` = Encrypts using public key.
- ``-i <identity-file>`` = uses private key for decryption. 

Other notes:

- The key file contains both public and private keys.
- Encryption uses only the public key. 
- Decryption uses both keys

## Removing Sensitive Data

Hard-Disk Drives:

Securely delete a file with ``shred``. This will overwrite the file with 
random data mutliple times, renames the file multiple times to obscure 
its original name, then deletes the file. This makes it very difficult 
for data recovery tools to extract meaningful information from the files.

``shred -u secret.txt``

- ``-u`` = truncate and delete the file after shredding.
- ``-n`` = number of times to overwrite (defualt is 3) ``shred -n 10 secret.txt``

For entire directories, you can use ``wipe``. 

``sudo apt install wipe`` and then ``wipe -r /path/to/directory/`` this will
remove the directory as well. If you want to keep the directory use 
``wipe -r /path/to/directory/*``

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


## In Practice

The best way to backup files are as follows:

Backup files: 

- ``rsync`` - command line, good for copying files incrementally to other folders 
or over ssh.
- ``rclone`` - just like ``rsync`` but for the cloud. Works with over 50 cloud providers
like Google Drive, Dropbox, OneDrive, etc.
- ``syncthing`` - Realtime file sync between your devices. Creates its own files
on each device and syncs changes between all devices. It is direct peer-to-peer file
sync, meaning there is no server hosting the files and copying between devices.

Good system:

1. Daily file backups to a local device like USB drive with ``rsync``.
2. Daily or weekly backups of files to remote with ``rclone``.

```cron
# backup to local drive
0 2 * * * rsync -rv --delete /srv/plex_media /mnt/usb/plex_media_backup

# backup to cloud
0 3 * * * rclone sync /srv/ gdrive:server-backup --log-file=/var/log/rclone.log

```

### Setup rclone

Create a config file to login to cloud provider:

```bash
# run rclone config wizard
rclone config

```
