# ARP-Spoofer

## ⚠ Disclaimer!!

### Use this at your own disretion. The developer *is not responsible* for any misuse of the tool.


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
    

*This is supported only on **UNIX** environment, but can be targetted against **any** system irrespective of it's OS.*

*To use this on any remote system, it is recommended to use a **Wireless adapter***

**To allow the victim system to access the internet, use the command below before ruuning this tool:**

    echo 1 > /proc/sys/net/ipv4/ip_forward

- [x] Completed
