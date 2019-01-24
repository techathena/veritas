from scapy.all import *
from scapy.layers.inet import TCP, IP

from scapy_http import http
import getip

from scapy import all
from scapy.all import *
import testfile
a = open("filepath.txt","r")
#dta stored in file using test .py  can be accesed using filevar
filevar = a.read()
a.close()
packets = scapy.all.rdpcap(filevar)

print(packets)


i = 0
for p in packets:
        i = i+1
#for ranges in dealinwithcsv.py
