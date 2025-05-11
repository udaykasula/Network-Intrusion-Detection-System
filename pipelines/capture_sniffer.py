from scapy.all import sniff
import requests
import json

def packet_callback(packet):
    packet_data = {
        "timestamp": str(packet.time),
        "src": packet[0][1].src,
        "dst": packet[0][1].dst,
        "proto": packet[0][1].proto,
        "len": len(packet)
    }
    response = requests.post("http://localhost:5000/predict", json=packet_data)
    print(response.json())

def start_sniffing():
    sniff(prn=packet_callback, store=0)

if __name__ == "__main__":
    start_sniffing()
