#!/usr/bin/env python

import subprocess

# import optparse
import re
import queue
from random import choice, randint

queue = queue.Queue()


def get_interface():
    all_interface = subprocess.check_output(["nmcli", "device", "status"]).decode('utf-8')

    return all_interface


def change_mac(interface, new_mac):

    subprocess.call(["ifconfig", interface[0], "down"])
    subprocess.call(["ifconfig", interface[0], "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface[0], "up"])

    return new_mac


def get_mac(interface):
    ifconfig_result = subprocess.check_output(['ifconfig', interface[0]]).decode('utf-8')
    mac_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    if mac_result:
        return mac_result.group(0)
    else:
        return "[-] Cound not find the MAC Address"


def random_mac(interface):
    cisco = ["00", "40", "96"]
    dell = ["00", "14", "22"]

    mac_address = choice([cisco, dell])
    for i in range(3):
        one = choice(str(randint(0, 9)))
        two = choice(str(randint(0, 9)))
        three = str(one + two)
        mac_address.append(three)
    newmac = ":".join(mac_address)

    return change_mac(interface, newmac)


def run_mac():
    current = "changemac"
    print(
        "Options: \n1.Show Interface: (showinterface) \n2.Show Current MAC Address: (currentmac) \n3.Set custom MAC Address: (setmac) \n4.Set random MAC Address: (setrandmac)"
    )
    while True:
        command = input("(currentmac)>> ")
        command = command.split(" ")
        try:
            if command[0] == "showinterface":
                print(get_interface())
            if command[0] == "currentmac":
                interface = input("Choose Interface: ")
                interface = interface.split(" ")
                print(get_mac(interface))
            if command[0] == "setmac":
                interface = input("Choose Interface: ")
                interface = interface.split(" ")
                newmac_inp = input("Provide New MAC Address: ")
                newmac_inp = newmac_inp.split(" ")
                change_mac(interface, newmac_inp)
                currentmac = get_mac(interface)
                if currentmac == newmac_inp:
                    print(("[+] MAC Address was changed sucessfully to " + current_mac))
                else:
                    print("[-] MAC Address did not get changed.")
            if command[0] == "setrandmac":
                interface = input("Choose Interface: ")
                interface = interface.split(" ")
                randmac = random_mac(interface)
                currentmac = get_mac(interface)
                if currentmac == randmac:
                    print(("[+] MAC Address was changed sucessfully to " + randmac))
                else:
                    print("[-] MAC Address did not get changed.")
            if command[0] == "exit":
                break
        except Exception:
            print("Error Executing Command")
