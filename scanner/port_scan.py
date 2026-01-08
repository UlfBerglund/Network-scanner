import nmap

def port_scan(host):
    """
    Scans a host for open TCP-ports
    and returns a list of port numbers.
    """
    nm = nmap.PortScanner()
    try:
        nm.scan(hosts=host, arguments="-sT")
    except Excepti
        return []
    open_ports = []

    for proto in nm[host].all_protocols():
        for port in nm[host][proto].keys():
            if nm[host][proto][port]['state'] == 'open':
                open_ports.append(port)
    open_ports.sort()
    return open_ports