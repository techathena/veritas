import scapy
from scapy import all
import getip
def briefinfo():
     a = open("filepath.txt","r")
     #dta stored in file using test .py  can be accesed using filevar
     filevar = a.read()
     a.close()
     brief = scapy.all.rdpcap(filevar)

     return(brief)
#tells no of packets with each protocol in pcap file
