#!/usr/bin/env python

import subprocess
import optparse
import re
import queue
from random import choice, randint

queue = queue.Queue()

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface for the Mac Changer")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC Address")
    parser.add_option("-r", "--random", dest ="rand_mac", help="Random MAC Address",action="store_true")
    (options, arguments)=parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more.")
    if not options.new_mac and not options.rand_mac:
        parser.error("[-] Please specify an new MAC Address, use --help for more.")

    return options


def get_interface():
    all_interface = subprocess.check_output(["nmcli", "device", "status"]).decode('utf-8')
    return all_interface

def change_mac(interface, new_mac):
    print(("[+] Changing MAC Address for " + interface + " to " + new_mac))

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface]).decode('utf-8')
    mac_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    if mac_result:
        return mac_result.group(0)
    else:
        return None
        print("[-] Cound not find the MAC Address")

def random_mac():
    cisco = ["00","40","96"]
    dell = ["00","14","22"]

    mac_address = choice([cisco,dell])
    for i in range(3):
        one = choice(str(randint(0,9)))
        two = choice(str(randint(0,9)))
        three = (str(one + two))
        mac_address.append(three)

    return ":".join(mac_address)

options = get_arguments()
print("MAC Changer\n\t-Alrocks29")
current_mac = get_mac(options.interface)
print(("Current MAC = " + str(current_mac)))
rand_mac = random_mac()
if current_mac:
    if options.new_mac:
        change_mac(options.interface, options.new_mac)
        current_mac = get_mac(options.interface)
    elif options.rand_mac:
        change_mac(options.interface, rand_mac)
        current_mac = get_mac(options.interface)


if current_mac==options.new_mac or current_mac==rand_mac:
    print(("[+] MAC Address was changed sucessfully to " + current_mac))
else:
    print("[-] MAC Address did not get changed.")




