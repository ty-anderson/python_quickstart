# Wireguard

Wireguard (wg) is an open source VPN software.

You'll need to update the docker compose file with your hosts public ip
and also create a bcrypt hashed password. You can do the password with
python like this:

```bash
python3 -m pip install bcrypt
python3 -c "import bcrypt; print(bcrypt.hashpw(b'yourpassword', bcrypt.gensalt()).decode())"
```

```yaml
volumes:
  etc_wireguard:

services:
  wg-easy:
    environment:
      # Change Language:
      # (Supports: en, ua, ru, tr, no, pl, fr, de, ca, es, ko, vi, nl, is, pt, chs, cht, it, th, hi, ja, si)
      - LANG=en
      # ⚠️ Required:
      # Change this to your host's public address
      - WG_HOST=<host.public.ip.address>

      # Optional:
      - PASSWORD_HASH=<password_hash>
      # - PORT=51821
      # - WG_PORT=51820
      # - WG_CONFIG_PORT=92820
      # - WG_DEFAULT_ADDRESS=10.8.0.x
      # - WG_DEFAULT_DNS=1.1.1.1
      # - WG_MTU=1420
      # - WG_ALLOWED_IPS=192.168.15.0/24, 10.0.1.0/24
      # - WG_PERSISTENT_KEEPALIVE=25
      # - WG_PRE_UP=echo "Pre Up" > /etc/wireguard/pre-up.txt
      # - WG_POST_UP=echo "Post Up" > /etc/wireguard/post-up.txt
      # - WG_PRE_DOWN=echo "Pre Down" > /etc/wireguard/pre-down.txt
      # - WG_POST_DOWN=echo "Post Down" > /etc/wireguard/post-down.txt
      # - UI_TRAFFIC_STATS=true
      # - UI_CHART_TYPE=0 # (0 Charts disabled, 1 # Line chart, 2 # Area chart, 3 # Bar chart)
      # - WG_ENABLE_ONE_TIME_LINKS=true
      # - UI_ENABLE_SORT_CLIENTS=true
      # - WG_ENABLE_EXPIRES_TIME=true
      # - ENABLE_PROMETHEUS_METRICS=false
      # - PROMETHEUS_METRICS_PASSWORD=$$2a$$12$$vkvKpeEAHD78gasyawIod.1leBMKg8sBwKW.pQyNsq78bXV3INf2G # (needs double $$, hash of 'prometheus_password'; see "How_to_generate_an_bcrypt_hash.md" for generate the hash)

    image: ghcr.io/wg-easy/wg-easy
    container_name: wg-easy-compose
    volumes:
      - etc_wireguard:/etc/wireguard
    ports:
      - "51820:51820/udp"
      - "51821:51821/tcp"
    restart: unless-stopped
    cap_add:
      - NET_ADMIN
      - SYS_MODULE
      # - NET_RAW # ⚠️ Uncomment if using Podman
    sysctls:
      - net.ipv4.ip_forward=1
      - net.ipv4.conf.all.src_valid_mark=1
```


Once the container is running you'll need to setup other machines to
have access. 

1. Go to the UI: http://<your-server-ip>:51821
2. Add Client. Name it something descriptive. wg-easy automatically:
   - Creates a new private/public key pair for that client
   - Assigns a VPN IP address
   - Generates a .conf file and a QR code
3. Connect Devices

### 🧑‍💻 **Desktop / Laptop**

1. Install **WireGuard**:

    * macOS → App Store (“WireGuard”)
    * Windows → [wireguard.com/install](https://www.wireguard.com/install/)
    * Linux → `sudo apt install wireguard`

2. In wg-easy, click **“Download config”** for your client.
   It’ll be a file like `tyler-laptop.conf`.

3. Open the WireGuard app → “Import Tunnel” → select that file.

4. Toggle **Activate** to connect.

---

### 📱 **Mobile (iPhone / Android)**

1. Install the official **WireGuard app**.
2. On the wg-easy dashboard, click **“Show QR code”** next to the client.
3. In the WireGuard app → “Add Tunnel” → “Scan from QR Code.”
4. Scan it, save, and toggle **Activate** to connect.

That’s it — your phone now routes through your home network via VPN!

---

## 🌎 4. Test the Connection

Once connected:

* Visit [https://ipinfo.io](https://ipinfo.io) — it should show **your home’s public IP**, not your phone/laptop’s local network IP.
* If you can reach internal devices like `192.168.x.x`, that means local routing is working too.

---

## ⚙️ 5. (Optional) Enable Port Forwarding

If you want to access wg-easy **from outside your LAN**:

* Forward **UDP port 51820** on your router → your server’s LAN IP.
* (Optionally) Forward **TCP 51821** if you want to reach the dashboard remotely.

    * Though best practice: leave 51821 closed and use a VPN client only.

---

## 🔐 6. Add More Clients Later

Each client is isolated, so you can add as many as you want:

* “Add client” → scan QR or download config → done.
  wg-easy handles all the routing automatically.

---
