"""Load an IP blocklist from a file and check addresses against it."""
import ipaddress

def load_blocklist(path):
    """Read a blocklist file and return a set of IP Addresses

    Blank lines and lines that start with # are skipped
    Raises ValueError if any line is not a valid IP Address
    """

    blocked = set()
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.startswith("#") or not line:
                continue
            blocked.add(ipaddress.ip_address(line))
        return blocked


def is_blocked(ip_string, blocklist):
    """Return True if ip_string is in the blocklist

    Raises ValueError if ip_string is not a valid ip address
    """
    ip = ipaddress.ip_address(ip_string)
    return ip in blocklist
