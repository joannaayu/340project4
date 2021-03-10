import subprocess
import sys

def get_ipv6_address(domain):
    result = subprocess.check_output(["nslookup", "-type=AAAA", domain, "8.8.8.8"],
          timeout=2, stderr=subprocess.STDOUT).decode("utf-8")

    result = result.replace('\t', '')
    result = result.replace('\n', ' ')
    result = result.split(' ')
    new_results_array = []


    for i in range(len(result)):
        if 'AAAA' in result[i]:
            new_results_array.append(result[i+2])

    return new_results_array
