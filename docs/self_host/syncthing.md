# Syncthing

syncthing - Realtime file sync between your devices. 
Creates its own files on each device and syncs changes between all devices. 
It is direct peer-to-peer file sync, meaning there is no server hosting 
the files and copying between devices. 

Whats the difference between samba and syncthing?

**TLDR:** Samba keeps a central place for files, and you need internet access. 
Syncthing stores copies of the files on each device and you can use them offline.

### 🧩 **Samba (or SMB file sharing)**

* Acts like a **network drive** or shared folder.
* Files **live in one place** (usually on your server).
* Other devices access them over the network.
* When you open or edit a file, it’s being read/written **directly on the server**.
* If you’re **offline** or disconnected from the network, you can’t access the files.
* Great for: centralized storage, multi-user access, shared drives.

🖥️ *Analogy:* Like a shared filing cabinet — everyone opens the same drawer to get files.

---

### 🔁 **Syncthing**

* Each device has its **own local copy** of the files.
* Changes on one device automatically **sync** to all others.
* You can work **offline** — edits will sync once devices reconnect.
* Works over local network or internet, with encryption.
* Great for: personal sync, backups, or distributed teams that need offline access.

📦 *Analogy:* Everyone has a copy of the same binder — when someone updates a page, everyone else’s binder updates too.

---

### ⚡ Summary comparison

| Feature        | Samba                   | Syncthing                        |
| -------------- | ----------------------- | -------------------------------- |
| File location  | Central server          | Each device has a copy           |
| Offline access | ❌ No                    | ✅ Yes                            |
| Sync direction | None (live access only) | Two-way sync                     |
| Network needed | Local (LAN)             | LAN or Internet (peer-to-peer)   |
| Use case       | Shared drive            | File replication / personal sync |
| Security       | LAN authentication      | End-to-end encryption            |
| Storage usage  | One copy on server      | Multiple copies across devices   |

---

* **Samba** = one shared “live” copy (best for collaboration on a central server).
* **Syncthing** = synced local copies (best for redundancy and offline access).

To use:

Install on each device you want to use it with: https://syncthing.net/

