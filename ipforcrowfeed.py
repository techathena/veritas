from scapy.layers.inet import TCP, IP
#used for ip in  threatcrowdfeed api for ip reputation

global ipvari

from scapy import all
from scapy.all import *
import testfile
a = open("filepath.txt","r")
#dta stored in file using test .py  can be accesed using filevar
filevar = a.read()
a.close()
packets = scapy.all.rdpcap(filevar)

print(packets)


for p in packets:
        if p.haslayer(IP):
             ipvari = p[IP].dst

