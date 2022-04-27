#!/usr/bin/env python3

import netifaces

print(netifaces.interfaces())

"""for i in netifaces.interfaces():
    print('\n****** details of interface - ' + i + ' ******')
    try:
        print('MAC: ', end='') # This print statement will always print MAC without an end of line
        print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr']) # Prints the MAC address
        print('IP: ', end='')  # This print statement will always print IP without an end of line
        print((netifaces.ifaddresses(i)[netifaces.AF_INET])[0]['addr']) # Prints the IP address
    except:          # This is a new line
        print('Could not collect adapter information') # Print an error message
"""

def get_ip(device):
    if device in netifaces.interfaces():
        print(f"IP Address: {(netifaces.ifaddresses(device)[netifaces.AF_INET])[0]['addr']}")
    else:
        print(f"{device} not found")

def get_mac(device):
    if device in netifaces.interfaces():
        print(f"MAC Address: {(netifaces.ifaddresses(device)[netifaces.AF_LINK])[0]['addr']}")
    else:
        print(f"{device} not found")

interface = input("Enter interface to get information:  ")
ip_or_mac = input("Would you like the ip address or mac address?  ")

if ip_or_mac.lower() == 'ip':
    get_ip(interface)
elif ip_or_mac.lower() == 'mac':
    get_mac(interface)
else:
    print("Not a valid option")
