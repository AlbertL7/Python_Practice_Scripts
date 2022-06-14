from ipaddress import ip_address
import datetime
import platform 
import os


ip_address = input("Enter IP address: ")

ip_split = ip_address.split(".")

network_ip = ip_split[0] + "." + ip_split[1] + "." + ip_split[2] + "."

first_in_range = int(input("input the the first number in the range you want to scan:  "))
last_in_range = int(input("input the last number in the range you want to scan:  "))

system = platform.system()

if system == 'Windows':
    ping = 'ping -n 1 '
else:
    pring = "ping -c 1 "

time1 = datetime.datetime.now()
if system == 'Windows':
    print(f'\nScanning Windows network for active IP addresses...\n\nstarted time: {time1}\n')
else:
    print(f'\nScanning Linux/Unix network for active IP addresses...\n\nstarted time: {time1}\n')

    
for ip in range(first_in_range,last_in_range):
    addr = network_ip + str(ip)
    command = ping + addr
    response = os.popen(command)
    read = response.readlines()
    
    for line in read:
        if(line.count("TTL")) or (line.count("ttl")):
            print(addr, "~~~~~Found!")
            break
    
time2 = datetime.datetime.now()    
total_time = time2 - time1

print('\nScanning Complete! in ', total_time)

