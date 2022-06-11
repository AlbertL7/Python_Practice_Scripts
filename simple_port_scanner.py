import socket
import datetime

target_host = input('Enter target IP Address: ')
scan_time = datetime.datetime.now() 

def port_scanner():
    try:
        print('Scanning ' + target_host + ' at ' + str(scan_time))
        for port in range(1,1025):
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = client.connect_ex((target_host,port))
            
            if result == 0:
                print(f'port {port} is open')
            else:
                pass
            
            client.close()
    except KeyboardInterrupt:
        print('\nThe scan has been terminated ' + str(scan_time))
    else:
        if result != 0:
            print('No open ports found, Scan complete ' + ' at ' + str(scan_time))
        else:
            print('\n Scan complete at:' + str(scan_time))
    
print(port_scanner())        
            
          
