# Networking

A network has many different things going on.

In networking, devices sit behind routers. Routers have a public IP address that
is used in accessing the internet, or a wide area network (WAN). The router also 
manages local ip address for all devices through DHCP. 

## DHCP
DHCP - Dynamic Host Configuration Protocol

DHCP is a server responsible for assigning local ip addresses to devices on the network. 
It can also have local domain names assigned, frequently setup as ``home.local`` or ``local``.

You can use DHCP to reserve certain ip addresses for certain devices.
You can also assign names that point to a certain device. This way you can refer to 
the device on the network by an easy to remember name instead of the ip address.
For example 192.168.1.104 -> homeserver.

When a device joins a network, it sends a "DHCP discover" message. 
A DHCP server responds to the message and assigns an IP address and other configuration information. 
DHCP also assigns new IP addresses when devices move to new locations. 

## DNS

DNS - Domain Name System

This translates IP addresses into domain names. Think of a phonebook for the internet. Instead
of names to phone numbers it points domain names to ip addresses. There are public DNS servers
that route the public domains on the internet. 

### Local DNS

There are also DNS servers that are run on a router or a local machine. This establishes
mappings from names to ip address only on your local network. This makes it so you can setup
a device with, say ip ``192.168.1.104`` to name ``mydevice.home``. Keep in mind that your 
router might have a suffix that attaches to these names, such as ``.home``

## IPv4 vs IPv6

### IPv4 

consists of devices having a 32-bit address that looks like 192.168.1.100.
It consists of public and private addresses, where the public addresses are
accessible over the internet and private addresses are only accessible over 
a local network. This means for data to get passed from one device over the internet
to another device, the protocol Network Area Translation (NAT) is used. NAT
will convert every packet of your private ip to the public which costs compute.

### IPv6

- 128-bit addresses, virtually infinite possible addresses.
- Device addresses are globally routable (not hidden behind a public IP).
- Because devices are globally routable, it eliminates the need for NAT 
as devices can connect end-to-end. Allowing for better connection
speeds for video, audio, peer-to-peer, gaming, etc.
- Devices can auto-configure with Stateless Address Autoconfiguration (SLAAC), no
need for DHCP.
- Firewalls are more relevant with IPv6 due to addresses being globally routable.

``ip -6 addr show``

Local address: ``fe80::``

- Scope: Local network segment (cannot be routed on the internet).
- Usage: Used for internal network functions like router discovery and neighbor discovery.
- Common for: Internal device communication.

Global address: Usually starts with ``2xxx::`` or ``3xxx::``

- Scope: Globally routable on the internet.
- Usage: For internet-facing applications or public communication.
- This is often the correct address for external access.

Address types:

- scope global → for internet or external routing.
- scope link → for local network only.

SSH: ssh user@[fe80::1a2b:3c4d:5e6f%eth0]


## Commands

``netstat`` - 
