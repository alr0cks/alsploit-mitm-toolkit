#!/usr/bin/python3
# import spoof.arpspoofer as arpspoof
# import spoof.dnsspoofer as dnsspoof
import features.changemac as changemac
# import threading
# import time
import curses

def logo():
    return f"""\033[92m
    /\   | |        / ____|     | |     (_) |    | \033[95m Welcome to AL-Sploit \033[92m
   /  \  | |  _____| (___  _ __ | | ___  _| |_   | \033[95m Version : {0.2} \033[92m
  / /\ \ | | |______\___ \| '_ \| |/ _ \| | __|  | \033[95m https://github.com/alrocks29\033[92m
 / ____ \| |____    ____) | |_) | | (_) | | |_   | \033[95m Author : Alrocks \033[92m
/_/    \_\______|  |_____/| .__/|_|\___/|_|\__|   
                          | |                  
                          |_|  
\033[0m
    """
    

def macchange():
    print("List of available Interfaces:\n")
    print(changemac.get_interface())
    interface = input("Enter the target interface:")
    current_mac = changemac.get_mac(interface)
    if current_mac == None:
        print("[-] Cound not find the MAC Address")
    else:
        print("[+]Current MAC Address: " + str(current_mac))
    print("Choose one of the following:")

print(logo())
