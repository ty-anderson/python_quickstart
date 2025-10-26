# General Architecture - Storage vs Compute

TLDR: Separate storage into a dedicated NAS and then use another server
for running programs on docker. Pull from and save to the NAS. A NAS should
not be used for compute processes.

---

## 🧩 The Core Idea: **Separate Compute from Storage**

> ⚙️ **Compute = running apps, containers, AI detection, transcoding, etc.**
> 💾 **Storage = reliable, redundant data layer (your NAS).**

When you keep these roles separate:

* Each system can specialize in what it does best.
* You reduce the risk of data loss or performance issues.
* It’s far easier to scale or troubleshoot later.

---

## 🧱 Why It’s Best to Keep NAS Dedicated

### 🧠 1. **NAS file systems (ZFS, Btrfs, etc.) are tuned for data integrity, not app workloads**

They protect your data through:

* checksums
* scrubbing
* snapshots
* RAID/parity

Running constant compute (e.g., Frigate writing video, or Immich generating thumbnails) can interfere with these optimizations and make rebuilds or snapshots slower.

---

### ⚡ 2. **CPU and memory resources get shared**

NAS tasks like ZFS compression, parity calculations, and indexing already use a fair bit of CPU/RAM.
If you also run:

* Frigate (AI inference + decoding)
* Immich (image processing + face recognition)
* or Jellyfin (video transcoding)

…then your NAS’s primary job — protecting and serving data — might get delayed or throttled.

---

### 🔒 3. **Stability and safety**

If one container crashes, hangs, or fills the filesystem, it can:

* Interrupt the NAS’s storage pools
* Corrupt running writes
* Even cause pool degradation if disks get overloaded

Keeping your NAS “clean” isolates your data from application risk.

---

## 🧠 The Professional Model (and the Smart Home-Lab Model)

| Layer                   | Purpose                              | Examples                               |
| ----------------------- | ------------------------------------ | -------------------------------------- |
| **Compute Layer**       | Run containers, AI, video processing | Frigate, Immich, Home Assistant, Plex  |
| **Storage Layer (NAS)** | Serve and protect data               | TrueNAS, Unraid, Synology, ZFS pool    |
| **Network Layer**       | Link them via fast Ethernet          | 1 Gb or 2.5 Gb+ LAN, NFS or SMB shares |

They’re connected by the network — the NAS exports shared folders, and the compute node mounts them.

---

### 🧩 Typical Setup Example

```
        ┌────────────────────┐
        │  Cameras / Clients │
        └────────┬───────────┘
                 │
            ┌────┴────┐
            │ Frigate │   ← Compute (Docker, GPU)
            │ Immich  │
            │ Plex    │
            └────┬────┘
                 │  (NFS/SMB)
        ┌────────┴────────┐
        │      NAS        │  ← Storage (ZFS/RAID, backups)
        │  TrueNAS / RAID │
        └─────────────────┘
```

---

## 🧩 When You *Can* Combine Them

It’s perfectly fine to run extra apps *on your NAS* if:

* It’s powerful (e.g., Xeon/i7 CPU, 32 GB+ RAM)
* You’re okay with minor slowdowns
* The apps aren’t CPU-intensive (e.g., photo viewer, simple sync service)

For example:

* Synology users often run Docker containers on the NAS directly (for convenience).
* Unraid and TrueNAS SCALE support running VMs or containers safely alongside storage — but it still shares the same hardware, so performance depends on your use case.

---

## ✅ In short

> For **maximum reliability and scalability**, yes — it’s best to have:
>
> * 🖥️ **One machine dedicated to compute** (Frigate, Immich, Plex, etc.)
> * 💾 **One machine dedicated to storage** (your NAS)

This mirrors how **enterprise datacenters** and **well-designed homelabs** are built — storage servers feed compute servers.

---

Would you like me to show what a **recommended 2-node home setup** looks like (with network speeds, mount types, and backup flow)? It’s a great visual for planning how to physically wire and configure it.
