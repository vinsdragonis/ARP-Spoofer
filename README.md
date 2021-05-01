# ARP-Spoofer

ARP spoofer is a tool that sends falsified ARP messages over a LAN.

## ⚠ Disclaimer!!

### Use this at your own discretion. The developer *is not responsible* for any misuse of the tool.


**To use this:**

    1. Clone this repository.
    2. Run netowrk_scanner.py
    3. Use arp_spoof.py if you have python2.x, else use arp_spoof3.py for python3 compatibility
    4. Set the target IP address. (ex. 10.0.2.15)
    5. Set the gateway IP address. (ex. 10.0.2.1)

**Dependencies:**

    scapy module
    time module
    sys module
    argparse module
    

*This is supported only on **UNIX** environment, but can be targetted against **any** system irrespective of it's OS*

**To allow the victim to access the internet, use the command below before ruuning this tool:**

    echo 1 > /proc/sys/net/ipv4/ip_forward

*Using this in conjunction with other tools, you can perform **Man In The Middle Attacks***

*To use this on any remote system, it is recommended to use a **Wireless adapter***

- [x] Completed
