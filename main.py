#!/usr/bin/env python3

import argparse

from scanner.ping_sweep import ping_sweep
from scanner.port_scan import port_scan


def parse_arguments():
    """
    Parse command-line arguments using argparse.
    Provides predefined scan options to improve performance.
    """
    parser = argparse.ArgumentParser(
        description="Network scanner using Nmap (ping sweep + TCP port scan)"
    )

    parser.add_argument(
        "network",
        help="Target network in CIDR format (e.g. 192.168.10.0/24)"
    )

    parser.add_argument(
        "--fast",
        action="store_true",
        help="Use faster scan settings (-T4, skip DNS resolution)"
    )

    parser.add_argument(
        "--top-ports",
        action="store_true",
        help="Scan only the most common TCP ports (--top-ports 100)"
    )

    parser.add_argument(
        "--custom",
        help='Provide custom nmap flags, e.g. "-T4 --top-ports 100 -n"'
    )

    return parser.parse_args()


def main():
    args = parse_arguments()

    # Default nmap flags
    nmap_flags = "-sT"

    # Apply predefined performance options
    if args.fast:
        nmap_flags += " -T4 -n"

    if args.top_ports:
        nmap_flags += " --top-ports 100"

    # Custom flags override everything
    if args.custom:
        nmap_flags = args.custom

    print(f"\n[*] Scanning network: {args.network}")
    print(f"[*] Using nmap flags: {nmap_flags}\n")

    hosts = ping_sweep(args.network)

    print(f"Active hosts ({len(hosts)}):")
    if len(hosts) == 0:
        print("No active hosts found.")
        return

    for host in hosts:
        open_ports = port_scan(host, nmap_flags)

        print(f"\nHost: {host}")
        if len(open_ports) > 0:
            ports = ", ".join(map(str, open_ports))
            print(f"Open TCP ports: {ports}")
        else:
            print("No open TCP ports found.")


if __name__ == "__main__":
    main()
