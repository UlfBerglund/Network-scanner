from scanner.ping_sweep import ping_sweep

if __name__ == "__main__":
    network = input("Enter network range (e.g: 192.168.1.0/24): ")
    hosts = ping_sweep(network)
    print("\nActive hosts:")
    for host in hosts:
        print(host)
