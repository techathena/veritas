
from scapy import all
from scapy.all import *

import getip


def removerep():
    makelist = []
    #remove repeating destination ip
    a = open("filepath.txt","r")
    #dta stored in file using test .py  can be accesed using filevar
    filevar = a.read()
    a.close()
    packets = scapy.all.rdpcap(filevar)

    for p in packets:
         ip = getip.ipvarikafun()
         makelist.append(ip)
    makedict = list(dict.fromkeys(makelist))
    counted = len(makedict)
    no = 0
    for elem in makedict:
         return(elem)


