#!/usr/bin/python3
import spoof.arpspoofer as arpspoof
# import spoof.dnsspoofer as dnsspoof
import features.changemac as changemac
import networkscan.netscan as netscan
import threading
import time

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
    


def run():
    current = "alsploit"
    # result = ""
    while True:
        command = input("(" + current + ")" + ">> ")
        command = command.split(" ")
        # try:
        if command[0]=="changemac":
            changemac.run_mac()
        
        if command[0]=="netscan":
            netscan.run_netscan()


        if command[0]=="arpspoof":
            t1=threading.Thread(target=arpspoof.arp_run())
            t1.start()
            # arpspoof.arp_run()


                    
        # except Exception:
            print("Error")
        # print(result)
print(logo())
run()
