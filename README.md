# Network Scanner (Ping Sweep & Port Scan)

This project is a simple network scanner written in Python.
It performs two main tasks:

1. Ping sweep to identify active hosts in a network
2. TCP port scanning of the discovered hosts using Nmap

The project is part of a course assignment and follows
a feature-branch workflow with multiple commits and three pull requests.

---

## Features

- Ping sweep using Nmap to detect active hosts
- Filters out network and broadcast addresses
- TCP connect scan (`-sT`) for open ports
- Optional command-line flags for enhanced performance
- Sorted list of open ports
- Timeout handling for faster scans
- Error handling to avoid crashes
- Clear and readable output

---

## Requirements

- Kali Linux (or Linux with Nmap installed)
- Python 3
- Nmap
- python-nmap library

Install dependencies:

```bash
pip install -r requirements.txt

## Usage:

- The script uses _argparse_ and is started from the command line.
- Basic scan:
python3 main.py network e.g. 192.168.10.0/24
- Fast scan:
python3 main.py 192.168.10.0/24 --fast
- Scan only common ports:
python3 main.py 192.168.10.0/24 --top-ports
- Custom Nmap flags:
python3 main.py 192.168.10.0/24 --custom "-T5 -n -p 22,80,443"
- Show help
python3 main.py -h

## Disclaimer
Only scan networks you own or have permission to test.