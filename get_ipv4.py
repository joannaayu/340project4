import subprocess
import sys

def get_ipv4_address(domain):
    result = subprocess.check_output(["nslookup", domain, "8.8.8.8"],
          timeout=2, stderr=subprocess.STDOUT).decode("utf-8")
    return result
