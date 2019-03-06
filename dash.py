import socket
import struct
import binascii
import time
import json
import urllib 

# Use your own IFTTT key
ifttt_key = 'cFCNXI3YWPpEyxL6Tir0WG'
# Set these up at https://ifttt.com/maker
ifttt_url_button = 'https://maker.ifttt.com/trigger/on_button_pressed/with/key/' + ifttt_key

# Replace this MAC addresses and nickname with your own
macs = {
    '6837E96BFC81' : 'on_button'
}

# Trigger a IFTTT URL. Body includes JSON with timestamp values.
def trigger_url(url):
    data = '{ "value1" : "' + time.strftime("%Y-%m-%d") + '", "value2" : "' + time.strftime("%H:%M") + '" }'
    req = urllib.Request(url, data, {'Content-Type': 'application/json'})
    f = urllib.urlopen(req)
    response = f.read()
    f.close()
    return response

def on_button_pressed():
    print("triggering button event, response: ") + trigger_url(ifttt_url_button)

rawSocket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.htons(0x0003))

while True:
    packet = rawSocket.recvfrom(2048)
    ethernet_header = packet[0][0:14]
    ethernet_detailed = struct.unpack("!6s6s2s", ethernet_header)
    # skip non-ARP packets
    ethertype = ethernet_detailed[2]
    if ethertype != '\x08\x06':
        continue
    # read out data
    arp_header = packet[0][14:42]
    arp_detailed = struct.unpack("2s2s1s1s2s6s4s6s4s", arp_header)
    source_mac = binascii.hexlify(arp_detailed[5])
    source_ip = socket.inet_ntoa(arp_detailed[6])
    dest_ip = socket.inet_ntoa(arp_detailed[8])
    if source_mac in macs:
        #print "ARP from " + macs[source_mac] + " with IP " + source_ip
        if macs[source_mac] == 'on_button':
            on_button_pressed()
    else:
        print ("Unknown MAC " + source_mac + " from IP " + source_ip )        