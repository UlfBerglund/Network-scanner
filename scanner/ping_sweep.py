import nmap

def ping_sweep(network):
    """ Scans a network and returns a list of active IP addresses. """
    nm = nmap.PortScanner()
    nm.scan(hosts=network, arguments="-sn")

    active_hosts = []

    for host in nm.all_hosts():
        if nm[host].state() == "up":
            active_hosts.append(host)

    return active_hosts
