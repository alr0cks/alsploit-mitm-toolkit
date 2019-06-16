# ARP Spoofer

The ARP Spoofer written in Python which makes the attacker a man in the middle over a network.

Arguments: -t Target ip address
           -s source ip address
Modules Used: scapy-python3
              sys

PS: Needs ip forwading transfer packets without loss
Just run this command in Terminal "echo 1 > /proc/sys/net/ipv4/ip_forward"

![arpspoof](/screenshot_spoof.png?raw=true "")
![arpspoof](/arp_table.PNG?raw=true "")
