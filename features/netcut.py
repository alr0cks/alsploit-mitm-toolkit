#!/usr/bin/env python

import netfilterqueue


def process_packets(packet):
    packet.drop()

def run_netcut():
    queue = netfilterqueue.NetfilterQueue()
    queue.bind(0, process_packets)
    queue.run()
