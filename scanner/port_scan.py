import nmap

def port_scan(host, nmap_flags):
    """
    Scans a host for open TCP-ports
    and returns a list of port numbers.
    """
    nm = nmap.PortScanner()
    try:
        nm.scan(hosts=host, arguments="-sV --host-timeout 30s")
    except Exception:
        return []
    
    results = []

    for proto in nm[host].all_protocols():
        for port in nm[host][proto].keys():
            if nm[host][proto][port]['state'] == 'open':
                service = nm[host][proto][port].get('name', 'unknown')
                product = nm[host][proto][port].get('product', '')
                version = nm[host][proto][port].get('version', '')

                info = f"{port}/{service} {product} {version}".strip()
                results.append(info)

    results.sort()
    return results
