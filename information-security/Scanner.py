#!/usr/bin/python3

import nmap

scanner = nmap.PortScanner()

print('Welcome, this is a simple nmap automation tool')
print('<------------------------------------------------>')

ip_addr = input('Please enter the IP address you want to scan: ')
print('The IP your entered is: ', ip_addr)
type(ip_addr)

resp = input(""" \nPlease enter the type of scan you want to run
                1) SYN ACK Scan
                2) UDP Scan
                3) Comprehensive Scan \n""")
print("You have selected option: ", resp)

if resp == '1':
    print("Nmap Version: ", scanner.nmap.version())
    scanner.scan(ip_addr, '1-1024', '-v -sS') # ip_address, ranges of ports to scan, type of scan - verbose and synax scan
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif resp == '2':
    print("Nmap Version: ", scanner.nmap.version())
    scanner.scan(ip_addr, '1-1024', '-v -sU') # ip_address, ranges of ports to scan, type of scan - verbose and synax scan
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['udp'].keys())
elif resp == '3':
    print("Nmap Version: ", scanner.nmap.version())
    scanner.scan(ip_addr, '1-1024', '-v -sS -sV -sC -A -O') # ip_address, ranges of ports to scan, type of scan - verbose and synax scan
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif resp >= '4':
    print("Please enter a valid option")
