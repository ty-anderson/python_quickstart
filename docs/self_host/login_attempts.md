# Important Commands

```bash
############################################################
# FAIL2BAN STATUS & OVERVIEW
############################################################

# Show all active jails (Fail2Ban services being monitored)
sudo fail2ban-client status

# Show detailed status for SSH jail: failures, bans, file watched
sudo fail2ban-client status sshd

# Show Fail2Ban version, active jails, global info
sudo fail2ban-client -v -v status sshd


############################################################
# REAL-TIME MONITORING (LIVE VIEW)
############################################################

# Watch Fail2Ban log in real time (bans, failures, regex matches)
sudo tail -f /var/log/fail2ban.log

# Live monitoring of SSH authentication logs
sudo tail -f /var/log/auth.log


############################################################
# VIEW BAN EVENTS
############################################################

# Show all ban events (including archived logs)
sudo zgrep -i "Ban" /var/log/fail2ban.log*

# Show all unban events
sudo zgrep -i "Unban" /var/log/fail2ban.log*

# List currently banned IP addresses
sudo fail2ban-client status sshd | grep -i "Banned IP list"


############################################################
# VIEW FAILED LOGIN ATTEMPTS (SYSTEM LOGS)
############################################################

# Show all failed SSH logins
sudo grep -i "failed password" /var/log/auth.log

# Show invalid username attempts
sudo grep -i "invalid user" /var/log/auth.log

# Show all authentication failures (ssh + sudo)
sudo grep -i "authentication failure" /var/log/auth.log

# Show failed attempts from a specific IP
sudo grep -i "failed" /var/log/auth.log | grep <IP>


############################################################
# OVERVIEW OF RECENT LOGIN ACTIVITY
############################################################

# Show successful logins (SSH + local)
last

# Show failed login attempts (from btmp)
sudo lastb

# Show all SSH login attempts in the last 12 hours
sudo journalctl -u ssh --since "12 hours ago"


############################################################
# ANALYZE BRUTE FORCE PATTERNS
############################################################

# Count failed attempts by IP (most frequent first)
sudo grep "Failed password" /var/log/auth.log \
  | awk '{print $(NF-3)}' | sort | uniq -c | sort -nr

# Count attempts by username (detect targeted accounts)
sudo grep "Failed password" /var/log/auth.log \
  | awk '{print $(NF-5)}' | sort | uniq -c | sort -nr

# Show top 20 offending IPs
sudo grep "Failed password" /var/log/auth.log \
  | awk '{print $(NF-3)}' | sort | uniq -c | sort -nr | head -20


############################################################
# CORRELATE FAIL2BAN BANS WITH AUTH.LOG ATTEMPTS
############################################################

# For each banned IP, print their matching authentication failures
sudo zgrep -i "Ban" /var/log/fail2ban.log* \
  | awk '{print $NF}' | sort | uniq | while read ip; do
      echo "----- Attempts from $ip -----"
      sudo grep $ip /var/log/auth.log
      echo
    done


############################################################
# MONITOR SYSTEM LOAD / QUEUES DURING ATTACKS
############################################################

# Check CPU load and process queue (sar requires sysstat installed)
sar -q

# View CPU usage over time
sar -u

# View memory usage over time
sar -r

# View disk I/O bottlenecks (very useful during brute-force DDoS)
iostat -xz 1 5


############################################################
# EXTRA: CHECK FIREWALL RULES FAIL2BAN ADDED
############################################################

# Show firewall rules currently applied (iptables)
sudo iptables -L -n

# Show nftables rules (Ubuntu 22+)
sudo nft list ruleset

```

## Fail2Ban

Fail2Ban **is one of the simplest, smartest, and most important security tools** you can put on an Ubuntu server — especially one exposed to SSH.

Think of it as:

> **A security guard that watches your logs and automatically blocks attackers.**

It’s lightweight, fast, and almost zero-maintenance once set up.

Let’s go deep — **but clearly** — so you truly understand it.

---

## 🛡️ **What Fail2Ban Does**

Fail2Ban:

1. **Watches system logs** (like `/var/log/auth.log` for SSH)
2. **Detects suspicious behavior**, such as:

    * repeated password failures
    * invalid users
    * repeated 404s (web servers)
    * bot scanning patterns
3. **Automatically bans the attacker’s IP** using `iptables`, `nftables`, or `firewalld`
4. **Unbans them later** (default 10 min)

This stops brute-force attacks dead.

---

## 🔍 **Fail2Ban in One Sentence**

> It monitors log files and bans any IP that fails too many times too quickly.

---

## 🚀 **Install Fail2Ban (Ubuntu)**

```
sudo apt update
sudo apt install fail2ban
```

This immediately protects SSH with default settings.

---

## 📦 **How It Works Internally**

Fail2Ban is built around:

* **Jails** → what service to monitor (e.g., sshd)
* **Filters** → regex rules to detect bad behavior
* **Actions** → what to do when triggered (e.g., block IP)
* **Log paths** → where to watch

---

## 🔒 **Key Fail2Ban Concepts**

### **1. Jail**

A *jail* is a configuration unit describing:

* log file to watch
* filter to use
* ban time
* max retries

Example jail (`sshd`):

```
[sshd]
enabled = true
port = ssh
filter = sshd
logpath = /var/log/auth.log
maxretry = 5
bantime = 600
```

---

### **2. Filter**

Filters contain regular expressions matching log failures.

Example (`/etc/fail2ban/filter.d/sshd.conf`):

```
failregex = ^%(__prefix_line)sFailed password for .* from <HOST>
```

When that regex matches logs too many times → ban.

---

### **3. Action**

Actions define what happens after a ban:

Typical action:

```
iptables -I INPUT -s <ip> -j DROP
```

In other words,
**the attacker’s packets die silently.**

Modern systems use `nftables`.

---

## 🔥 **What Fail2Ban Protects Against**

✔ SSH brute-force
✔ bots trying random usernames
✔ scanning for WordPress or PHPMyAdmin
✔ HTTP request floods (light protection)
✔ SMTP brute-force
✔ Nextcloud login failures
✔ Jupyter Notebook login failures
✔ anything with logs

---

## 🧠 **Why Fail2Ban Is Loved**

#### **✓ Protects every server automatically**

Millions of bots scan the internet 24/7. Fail2Ban keeps them out.

#### **✓ Extremely low overhead**

It’s tiny — it barely uses memory or CPU.

#### **✓ Very configurable**

You can write jails for custom apps or logs.

#### **✓ No weird firewall rules**

Fail2Ban adds temporary bans — safer than permanent blocks.

#### **✓ Zero maintenance**

Install → configure → forget.

---

## 🛠️ **Basic Configuration**

Always edit this file (not the defaults):

```
sudo nano /etc/fail2ban/jail.local
```

Example good configuration:

```
[DEFAULT]
bantime = 30m
findtime = 10m
maxretry = 5
banaction = nftables-multiport

[sshd]
enabled = true
port = ssh
logpath = /var/log/auth.log
backend = systemd
```

Then apply:

```
sudo systemctl restart fail2ban
```

---

## 👀 **Check Fail2Ban Status**

#### All jails:

```
sudo fail2ban-client status
```

#### Check the SSH jail:

```
sudo fail2ban-client status sshd
```

Example output:

```
Status for the jail: sshd
|- Filter
|  |- Currently failed: 1
|  |- Total failed:     248
|  `- File list:        /var/log/auth.log
`- Actions
   |- Currently banned: 7
   |- Total banned:     104
   `- Banned IP list:   162.243.12.43 185.22.44.9 ...
```

---

## 📅 **See who has been banned**

```
sudo zgrep "Ban" -h /var/log/fail2ban.log*
```

---

## 🔥 **Bonus: Protect Against Password Guessing Even When They Use Valid Username**

Add to `sshd` jail:

```
ignoreip = 192.168.1.0/24
maxretry = 4
findtime = 10m
bantime = 24h
```

And also add:

```
[sshd-ddos]
enabled = true
filter = sshd-ddos
port = ssh
logpath = /var/log/auth.log
maxretry = 2
```

This catches bots that open **many new SSH sessions at once** (DDoS style).

---

## 🔒 Want Maximum Security?

(optional but recommended)

### **1. Change SSH port**

Stops ~95% of bots.

```
sudo nano /etc/ssh/sshd_config
Port 2222
```

Restart SSH:

```
sudo systemctl restart ssh
```

### **2. Disable password authentication (only SSH keys)**

```
PasswordAuthentication no
```

### **3. Add fail2ban + key-only = unbeatable combo**

---

## If you want:

I can help you:

* configure the ideal `jail.local` for your server
* check your current SSH brute-force attempts
* tune the ban times
* whitelist your LAN
* secure Docker containers or any app logs you want protected

Just tell me how you want to use it!
