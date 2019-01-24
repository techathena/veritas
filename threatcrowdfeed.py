import requests, _json
import getip
from scapy.all import *
from scapy.layers.inet import TCP, IP
import ipforcrowfeed

#uses threatcrowd api for feeds
def threatfeed():
    threat_feed = []
    for p in getip.packets:

        getrbyip = requests.get("http://www.threatcrowd.org/searchApi/v2/ip/report/", {"ip": ""+ipforcrowfeed.ipvari}).text

        threat_feed = getrbyip
    return threat_feed
