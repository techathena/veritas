import csv
import threatcrowdfeed
import getip
import ranges

from scapy import all
from scapy.all import *
import reverse_IP

a = open("filepath.txt","r")
#dta stored in file using test .py  can be accesed using filevar
filevar = a.read()
a.close()
packets = scapy.all.rdpcap(filevar)



def write_csv():
    with open(r'file1.csv','w') as writefile:
      writer =csv.writer(writefile)

      for i in range(ranges.i):
                writing = [getip.getipf(),getip.getprotocol() ,threatcrowdfeed.threatfeed(),reverse_IP.geturl(),]
                writer.writerow(writing)
    print('Data stored')
    return()


