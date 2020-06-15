import scapy.all as scapy
def get_mac(ip):

    # Here, we are creating an ARP request ourselves to ask who has the specific IP we asked for.
    arp_request = scapy.ARP(pdst=ip)
    # print(arp_request)

    # Here, we are setting our destination MAC to broadcast MAC address to make sure
    # it is sent to all the clients who are on the same network
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    # This variable is your packet that will be sent across the network, as it contains information about MAc and ARP
    arp_request_broadcast = broadcast/arp_request
    # print(arp_request_broadcast)
    answered_list = scapy.srp(arp_request_broadcast, timeout=2, verbose = False)[0]
    # print(answered_list)
    for element in answered_list:
        print(element)
        print(element[1].hwsrc)
    # srp stands for send and receive packet.

    # return answered_list[0][1].psrc

get_mac("192.168.43.61")