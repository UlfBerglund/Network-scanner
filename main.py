#!/usr/bin/env python3

from scanner.ping_sweep import ping_sweep
from scanner.port_scan import port_scan

if __name__ == "__main__":
    network = input("Enter network range (e.g: 192.168.1.0/24): ")
    hosts = ping_sweep(network)
    print(f"\nActive hosts ({len(hosts)}):")
    if len(hosts) == 0:
        print("No active hosts found.")
    for host in hosts:
        open_ports = port_scan(host)
        if len(open_ports) > 0:
            print(host)
            print(f" Open ports: {', '.join(map(str, open_ports))}")
        else:
            print(" No open TCP ports found")

