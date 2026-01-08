# Network Scanner (Ping Sweep & Port Scan)

This project is a simple network scanner written in Python.
It performs two main tasks:

1. Ping sweep to identify active hosts in a network
2. TCP port scanning of the discovered hosts using Nmap

The project is part of a course assignment and follows
a feature-branch workflow with multiple commits and three pull requests from a peer.

---

## Features

- Ping sweep using Nmap to detect active hosts
- Filters out network and broadcast addresses
- TCP connect scan (`-sT`) for open ports
- Sorted list of open ports
- Timeout handling for faster scans
- Error handling to avoid crashes
- Clear and readable output

---

## Requirements

- Linux (tested on Kali Linux)
- Python 3
- Nmap
- python-nmap library

Install dependencies:

```bash
pip install python-nmap
