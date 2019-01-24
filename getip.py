import ftplib
from smtplib import SMTP

from dpkt.dns import DNS

from scapy.layers.dhcp import DHCP
from scapy.layers.inet import TCP, IP, UDP, ICMP

global ipvari

from scapy import all
from scapy.all import *
#import testfile
a = open("filepath.txt","r")
#dta stored in file using test .py  can be accesed using filevar
filevar = str(a.readline())
a.close()
packets = scapy.all.rdpcap(filevar)

print(packets)


#This function is in order to get ipvari as output


def ipvarikafun():
    for p in packets:
        if p.haslayer(IP):
             ipvari = p[IP].dst

        return ipvari
def getipf():
#returns both source and destination ip address
    ipvar =[]

    src_ip=[]
    for p in packets:

             if p.haslayer(IP):
                  src_ip =p[IP].src
                  ipvar = p[IP].dst
    return ipvar, src_ip

#getprotocol
def getprotocol():
    protocol_name = []
    for p in packets:
            if p.haslayer(TCP):
                print('TCP')
                protocol_name.append('/TCP')
            if p.haslayer(UDP):
                 print('UDP')
                 protocol_name.append(r'/UDP')
            if p.haslayer(ICMP):
                  print('ICMP')
                  protocol_name.append(r'/ICMP')
            if p.haslayer(ftplib.FTP):
                 print('FTP')
                 protocol_name.append((r'/FTP'))
            if p.haslayer(DNS):
                 print('DNS')
                 protocol_name.append(r'/DNS')
            if p.haslayer(SMTP):
                 print('SMTP')
                 protocol_name.append(r'/SMTP')
            if p.haslayer(DNS):
                 print('DNS')
                 protocol_name.append(r'/DNS')
            if p.haslayer(DHCP):
                 print('DHCP')
                 protocol_name.append(r'/DHCP')


    return(protocol_name)




