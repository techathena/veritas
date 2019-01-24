#this module uses gethostbyip function to get urls from the ip address
from _socket import gethostbyaddr
from scapy import all
from scapy.all import *
from scapy.layers.inet import TCP, IP


import getip
a = open("filepath.txt","r")
#dta stored in file using test .py  can be accesed using filevar
filevar = a.read()
a.close()

packets = scapy.all.rdpcap(filevar)

print(packets)

for p in packets:
        if p.haslayer(IP):
            ipadress = p[IP].dst
            try:
                 a = gethostbyaddr(str(ipadress))
                 print(a)


            except socket.error:
                print('error in getting address')
