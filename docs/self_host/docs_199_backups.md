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

# ── RSYNC FLAGS
# -v  verbose mode
# -a  archive mode (preserves permissions/timestamps)
# -z  compress files
# -e  specify remote shell command
# -r  recursive (copy subdirectories)
# -h  human-readable file sizes
# --progress  show progress
# --delete    remove files in dest not in source
# --exclude   exclude files (e.g., --exclude='*.log' --exclude='/cache/')
```

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

# ── TAR FLAGS
# -c  create new archive
# -v  verbose
# -f  specify archive filename
# -x  extract
# -z  gzip compression
```

## Encryption

``age`` is a lightweight focused encryption software for files. 
It uses modern cryptography making it more secure, but less featured 
than something like ``gpg``. Age  lets you use passwords or key files.

```bash
# ───────────────────────────────
# 🔐 ENCRYPTION (AGE)
# ───────────────────────────────

# Install age
brew install age           # macOS
sudo apt install age       # Linux

# Option 1: Password Encryption (simple)
age -o myfile.txt.age -p myfile.txt
age -d myfile.txt.age > myfile.txt

# Option 2: Public/Private Key Encryption (secure)
age-keygen -o ~/.age-key.txt     # create key file
age -r PUBLIC_KEY -o myfile.txt.age myfile.txt
age -d -i ~/.age-key.txt myfile.txt.age > myfile.txt

# Encrypt using key file directly
age -r $(head -n 1 ~/.age-key.txt) -o myfile.txt.age myfile.txt
age -d -i ~/.age-key.txt myfile.txt.age > myfile.txt

# Encrypt directory (tar + age)
tar -czf myfolder.tar.gz myfolder/
age -o myfolder.tar.gz.age -p myfolder.tar.gz

# One-liner: tar and encrypt simultaneously
tar -czf - myfolder/ | age -o myfolder.tar.gz.age -p

# Decrypt and extract in one step
age -d myfolder.tar.gz.age | tar -xz

# Manual decrypt
age -d myfolder.tar.gz.age > myfolder.tar.gz
tar -xzf myfolder.tar.gz
shred -u myfolder.tar.gz

# ── AGE FLAGS
# -o <output>     specify output file
# -d              decrypt
# -p              use password mode
# -r <pubkey>     encrypt with public key
# -i <identity>   specify private key for decryption
```

Other notes:

- The key file contains both public and private keys.
- Encryption uses only the public key. 
- Decryption uses both keys

## Removing Sensitive Data

```bash
# ───────────────────────────────
# 🧹 REMOVING SENSITIVE DATA
# ───────────────────────────────

# ── HDD: Use shred
shred -u secret.txt
shred -n 10 secret.txt

# -u  delete file after shredding
# -n  overwrite N times (default 3)

# ── Directories: Use wipe
sudo apt install wipe
wipe -r /path/to/directory/
wipe -r /path/to/directory/*  # keep directory but delete contents

# ── SSD: Use fstrim or srm
sudo fstrim -v /              # clears free space on SSD

# Secure delete tools
sudo apt install secure-delete  # Ubuntu/Debian
brew install srm                # macOS

srm -v my_secret_file.txt       # securely delete a file
wipe -rf my_secret_folder/      # securely delete a folder


# ───────────────────────────────
# 🧠 IN PRACTICE
# ───────────────────────────────
# Recommended workflow:

# - rsync → for incremental local backups
# - rclone → for cloud backups
# - syncthing → for live sync between devices (peer-to-peer)

# 🔁 Good routine:
# 1. Daily rsync to local drive
# 2. Daily/weekly rclone to cloud

# ── Example cron jobs
0 2 * * * rsync -rv --delete /srv/plex_media /mnt/usb/plex_media_backup
0 3 * * * rclone sync /srv/ gdrive:server-backup --log-file=/var/log/rclone.log

# Setup rclone
rclone config
```