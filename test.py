#!/usr/bin/python3
import spoof.arpspoofer as arpspoof
# import spoof.dnsspoofer as dnsspoof
import features.changemac as changemac
import networkscan.netscan as netscan
import threading
import time
    


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
            target_ip = input("(arpspoof) Enter Target IP >> ")
            gateway_ip = input("(arpspoof) Enter Gateway IP >> ")
            t1=threading.Thread(target=arpspoof.arp_run, args=(target_ip,gateway_ip))
            t1.setDaemon(True)
            t1.start()


                    
        # except Exception:
            print("Error")
        # print(result)
run()
