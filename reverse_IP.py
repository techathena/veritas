import requests, _json

import rem_rep_ip
from scapy.layers.inet import TCP, IP
#uses whoisxmlapi for getting url from ip address
def geturl():
    model_ips = requests.get('https://reverse-ip-api.whoisxmlapi.com/api/v1?apiKey=at_DfmsCxuG8yhIRetxCtXftBzhEnafy&ip='+rem_rep_ip.removerep())
    ips = dict(model_ips.json())
    urls = ips['result']
    for url in urls:
        return(url['name'])
print(geturl())
