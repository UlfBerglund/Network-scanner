from scanner.ping_sweep import ping_sweep

if __name__ == "__main__":
    network = input("Enter network range (e.g: 192.168.1.0/24): ")
    hosts = ping_sweep(network)
    print(f"\nActive hosts ({len(hosts)}):")
    if len(hosts) == 0:
        print("No active hosts found.")
    for host in hosts:
        print(host)
