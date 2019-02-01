
from scapy import all
from scapy.all import *

import getip
import csv
import threatcrowdfeed


#def removerep():
makelist = []
    #remove repeating destination ip
    #a = open("filepath.txt","r")
    #dta stored in file using test .py  can be accesed using filevar
    #filevar = a.read()
    #a.close()
packets = scapy.all.rdpcap(r"C:\Users\Jagmohan\Desktop\1.pcapng")

for p in packets:
         ip = getip.ipvarikafun()
         makelist.append(ip)

makedict = list(dict.fromkeys(makelist))
counted = len(makedict)
no = 0
for elem in makedict:
    with open(r'file1.csv','w') as writefile:
          writer =csv.writer(writefile)
          writing = [getip.getipf(),threatcrowdfeed.threatfeed()]
          writer.writerow(writing)

         #return(elem)


