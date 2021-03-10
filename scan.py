import json
import sys
import time
import subprocess
from get_ipv4 import *
from get_ipv6 import *
from insecure_http import *

input_file = sys.argv[1]
domain_dict = {}
scan_type = ['scan_time']
output_file = sys.argv[2]

with open(input_file, "r") as input:
    for line in input:
        domain = line.rstrip()
        i = 0
        scan_dict = {}
        while i<len(scan_type):
                scan_dict[scan_type[i]] = float(time.time())
                i = i + 1
        ipv4 = get_ipv4_address(domain)
        ipv6 = get_ipv6_address(domain)
        insecure = get_insecure_http(ipv4[0])

        scan_dict["ipv4_addresses"] = ipv4
        scan_dict["ipv6_addresses"] = ipv6
        scan_dict["insecure_http"] = insecure


        domain_dict[domain] = scan_dict

# for domain in domain_dict:

out_file = open(output_file, "w")
json.dump(domain_dict, out_file, sort_keys=False, indent=4)
out_file.close()
