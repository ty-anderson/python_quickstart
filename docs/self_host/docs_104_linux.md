# Linux

## Execute files

```bash
./path/to/file
# or
source /path/to/file
```

- ``./bash_script.sh`` executes the script as a standalone process. This method requires execute permissions.
- ``source bash_script.sh`` executes the script in the existing process (doesn't create standalone process). Allows
modifying environment variables in the current shell. Allows ``cd`` command to change directory.

TLDR: default to using ``source`` to execute files.

## File Permissions

```bash
# view permissions
ls -l  # <--view permissions of files in the directory.
ls -ld  # <--view permissions of the directory itself.

# change permissions - full read write all access
sudo chmod -R 777 /path/to/folder

```

View permissions:

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

```bash
# ───────────────────────────────
# 🔑 PERMISSIONS & OWNERSHIP REFERENCE
# ───────────────────────────────

# ── VIEW PERMISSIONS
ls -l          # list files with permissions
ls -ld folder  # view folder permissions only
stat filename  # detailed view (shows numeric + symbolic modes)


# ───────────────────────────────
# 🧭 ALTER PERMISSIONS (CHMOD)
# ───────────────────────────────
# chmod = change mode (permissions)
# Two methods: symbolic and numeric

# ── SYMBOLIC MODE
# u = user (owner)
# g = group
# o = others
# a = all (u+g+o)
# + = add permission
# - = remove permission
# = = set exact permission

# ▶️ Common examples
chmod u+rwx,g+r,o-r filename     # give user full, group read, remove read for others
chmod u+rwx filename             # owner full permissions
chmod g-w filename               # remove write for group
chmod o-r filename               # remove read for others
chmod +x filename                # give everyone execute permission
chmod a+r foldername             # allow all users to read a folder
chmod a-x script.sh              # remove execute for everyone


# ── NUMERIC (OCTAL) MODE
# Each permission type (r=4, w=2, x=1)
# Add them up for each role (user, group, others)

# Example table:
# r-- = 4, rw- = 6, rwx = 7, --- = 0
# Format: chmod [user][group][others] file

chmod 777 file    # rwx for all
chmod 755 file    # rwx for owner, r-x for group/others
chmod 700 file    # rwx for owner only
chmod 644 file    # rw for owner, r for group/others
chmod 600 file    # rw for owner, no access for others

# ▶️ Directories often use 755
chmod 755 /srv/web_apps
# Files typically use 644
chmod 644 index.html


# ───────────────────────────────
# 👑 CHANGE OWNERSHIP (CHOWN)
# ───────────────────────────────
# chown = change owner (and optionally group)

# ▶️ Change owner of a file
sudo chown user file.txt

# ▶️ Change owner and group
sudo chown user:group file.txt

# ▶️ Change owner recursively for directory and contents
sudo chown -R user:group /srv/web_apps

# ▶️ View ownership
ls -l filename
# Output: owner and group are shown in the middle columns


# ───────────────────────────────
# 🧩 OTHER USEFUL COMMANDS
# ───────────────────────────────
# Change only the group of a file
sudo chgrp groupname file.txt

# Add user to group (to give access)
sudo usermod -aG groupname username

# Check which groups a user belongs to
groups username

# Apply same permissions to all files in a directory
chmod -R 644 /srv/web_apps
# Apply directory execute bit so users can enter directories
find /srv/web_apps -type d -exec chmod 755 {} \;

# ───────────────────────────────
# ✅ TIPS
# ───────────────────────────────
# • Always test permissions with 'ls -l' after changes.
# • Directories need execute (x) permission to be accessible.
# • Use numeric mode for scripts or automation, symbolic for clarity.
# • For public web directories, 755 for folders and 644 for files is standard.
```

## Copy Directory

Two baked-in commands are ``scp`` or ``rsync``.

Here's an example with scp: ``scp -r ./site user@server:/srv/web_apps``.

**rsync is typically recommended over scp.**

Rsync usually comes on Linux and MacOS. 

```bash
# ───────────────────────────────
# 🧭 RSYNC COMMAND REFERENCE
# ───────────────────────────────

# ▶️ Basic usage
rsync -v /source/file/name.txt /dest/file

# ▶️ Use literal string (preserve special characters)
rsync -v '/source/file/na$me.txt' /dest/file

# ▶️ Send multiple files
rsync -v /source/file1.txt /source/file2.txt '/dest'

# ▶️ Send over SSH
rsync -av /source/file/name.txt user@server:/dest/file

# ▶️ Send over SSH with custom port
rsync -avz -e "ssh -p 2222" /source/file/name.txt user@server:/dest/file

# ▶️ Send over SSH with sudo on remote
rsync -v --rsync-path="sudo rsync" yt_download_image.tar user@server:/srv/flask_yt_download

# ▶️ Send entire directory (keeps parent folder)
rsync -avz /source/dir /dest/dir

# ▶️ Send all files *inside* a directory (no parent folder)
rsync -avz /source/dir/ /dest/dir

# ▶️ Full example with sudo and custom SSH port
rsync -avz --rsync-path="sudo rsync" -e "ssh -p 2222" /Users/tyleranderson/Bonus tyler@anderson.home:/home/tyler/backup

# ▶️ Full example with sudo (default port)
rsync -avz --rsync-path="sudo rsync" /Users/tyleranderson/Bonus tyler@anderson.home:/home/tyler/backup


# ───────────────────────────────
# ⚙️ FLAGS
# ───────────────────────────────
# -v            verbose mode
# -a            archive mode (preserves permissions, timestamps, symlinks)
# -z            compress files during transfer
# -e            specify remote shell (e.g., "ssh -p 2222")
# --progress    show transfer progress
# --delete      delete files in destination that are not in source
# --exclude     exclude specific files or folders (e.g., --exclude='*.log' --exclude='/cache/')


# ───────────────────────────────
# 📁 DIRECTORY COPY EXAMPLES
# ───────────────────────────────
# Copy directory into another (keeps 'site' folder)
rsync -av ./site user@server:/srv/web_apps/notes

# Copy directory contents into another (no 'site' folder)
rsync -av ./site/ user@server:/srv/web_apps/notes/
# Note: trailing “/” on source copies contents only; trailing “/” on destination does not matter.
```

## Tar Files

A tar file (.tar) is an archive that bundles multiple files or directories
into one file (optionally compressed). Commonly used for backups or transfers
on Linux and Unix systems.

```bash
# ───────────────────────────────
# 📦 TAR FILE COMMAND REFERENCE
# ───────────────────────────────

# ▶️ Create a tar file (no compression)
tar -cvf archive.tar /path/to/files/

# ▶️ Extract a tar file
tar -xvf archive.tar

# ▶️ Create a compressed tar file (.tar.gz)
tar -czvf archive.tar.gz /path/to/files/

# ▶️ Extract a compressed tar file
tar -xzvf archive.tar.gz

# ▶️ List files inside a tar file (without extracting)
tar -tvf archive.tar

# ▶️ Extract a specific file from a tar archive
tar -xvf archive.tar file.txt


# ───────────────────────────────
# ⚙️ FLAGS
# ───────────────────────────────
# -c   create a new archive
# -v   verbose mode (show progress)
# -f   specify the archive filename
# -x   extract from an archive
# -z   compress/decompress using gzip
```

## Encryption

```bash
# ───────────────────────────────
# 🔐 ENCRYPTION & SECURE DELETION REFERENCE
# ───────────────────────────────

# ── ENCRYPTION (AGE)
# age is a modern, lightweight encryption tool for files.
# It’s simpler and more secure than GPG, but with fewer features.

# ▶️ Encrypt a single file
age -o secretfile.age -p secretfile.txt

# ▶️ Encrypt a directory (use tar first)
tar -czf myfolder.tar.gz myfolder/
age -o myfolder.tar.gz.age -p myfolder.tar.gz

# ▶️ Install age
# macOS:
brew install age

# Ubuntu / Debian:
sudo apt install age


# ───────────────────────────────
# 🧹 REMOVING SENSITIVE DATA
# ───────────────────────────────

# ── HARD DISK DRIVES (HDD)
# Use 'shred' to securely delete files by overwriting with random data multiple times.

# ▶️ Securely delete a file
shred -u secret.txt

# ▶️ Overwrite file multiple times before deleting
shred -n 10 secret.txt

# ⚙️ FLAGS
# -u   truncate and delete file after shredding
# -n   number of overwrite passes (default is 3)


# ───────────────────────────────
# ⚡ SOLID STATE DRIVES (SSD)
# ───────────────────────────────

# ▶️ 1. Use fstrim (best for clearing free space on SSD)
# Tells SSD to permanently erase deleted data
sudo fstrim -v /

# ▶️ 2. Use srm or wipe (best for secure file deletion)
# Better than shred for SSDs (handles wear leveling properly)

# 🔹 Install secure delete tools
sudo apt install secure-delete    # Debian/Ubuntu
brew install srm                  # macOS

# 🔹 Securely delete a file
srm -v my_secret_file.txt

# 🔹 Securely delete a directory
wipe -rf my_secret_folder/
```

