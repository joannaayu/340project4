import json
import sys
import time
import subprocess
from get_ipv4 import *
from get_http_server import *
from get_insecure_http import *
from get_redirect import *

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
        domain_dict[domain] = scan_dict

        ipv4 = get_ipv4_address(domain)
        domain_dict[domain]["ipv4_addresses"] = ipv4
        #
        # http_server = get_http_server(domain)
        # domain_dict[domain]["http_server"] = http_server

        insecure = get_insecure(domain)
        domain_dict[domain]["insecure_http"] = insecure

        redirect = get_redirect(domain)
        domain_dict[domain]["redirect_to_https"] = redirect



#print(get_http_server(domain))

out_file = open(output_file, "w")
json.dump(domain_dict, out_file, sort_keys=False, indent=4)
out_file.close()