#!/usr/bin/env python

import scapy.all as scapy


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, verbose=False, timeout=10)[0]

    client_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        client_list.append(client_dict)
    return client_list


def run_netscan(command):
    while True:
        try:
            result = scan(command)
            print("IP\t\t\tMAC Address\n-------------------------------------")
            for client in result:
                print((client["ip"] + "\t\t" + client["mac"]))

            break
        except Exception:
            print("Error in Execution")
