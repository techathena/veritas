# veritas
This is a python software which reads and analyses pcap files.
This projet uses scapy for reading files  and a lot of other stuff.
It uses whois Reverse IP/DNS API which you can get at https://reverse-ip-api.whoisxmlapi.com/ to get the urls from destination ip adresses.
It uses threatcrowd for IP/URL reputation.You can find it at https://github.com/AlienVault-OTX/ApiV2



Now onto the major modules of the project:

1. testfile :
   This is used to enter the path of the pcap file Which is to be analysed.

2. newtestfile: 
  Its the one which will run the project.It will give you protocols,source IP,destination IP,IP Reputation,URL's accessed in a csv file.

3. file1.csv:
  This is the file which is currently saving the outputs.

4. threatcrowdfeed:
  This will access the threatcrowd api to give the feeds.

5. dealinwithcsv:
  Creates the csv file with outputs

6.getip:
  Gets source and destination IP adresses of a packet as well as the protocols.

7.reverseip:
  Gets the URL's from the Destination IP addresses.

8.filepath.txt:
  stores the path of pcap file to be read
  
  Feel free to contact me for more questions.Just send a pull request!


Note :This is a prototye version of the project.

  
