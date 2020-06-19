# Man-In-The-Middle Attack Toolkit

<hr />

### Installation:

```bash
$ git clone https://github.com/alrocks29/alsploit-mitm-toolkit.git
$ cd alsploit-mitm-toolkit
```
<hr />

Install necessary packages:
```bash
apt-get install build-essential python-dev libnetfilter-queue-dev
```

Install python libraries:
```bash
$ pip install -r requirements.txt
```

Execue the following command to enable packet forwarding:
```bash
$ echo 1 > /proc/sys/net/ipv4/ip_forward
```

Usage:
```bash
$ python3 Main.py
```

<hr />

### Modules:
```
changemac   :Change MAC Address.
netscan   :Scan network for possible active devices.
arpspoof    :Spoof target with ARP requests.
dnsspoof    :Spoof target with DNS (In Progress).
sniff   :Sniff targets (Currently works with HTTP only HTTPS (In progress)).
fintercept    :Replace downloadable files with trojons.
injectjs    :Inject jsvascript code in websites.
wififap    :Start Fake Access Point.
```
<hr />

Many features to be added soon.




