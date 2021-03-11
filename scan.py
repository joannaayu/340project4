import json
import sys
import time
import subprocess
import OpenSSL
from OpenSSL import SSL
import geoip2.database
from get_ipv4 import *
from get_ipv6 import *
from get_http_server import *
from get_insecure_http import *
from get_redirect import *
from get_tls_versions import *
from get_root_ca import *
from get_hsts import *
from get_rdns import *
from get_rtt import *
from get_geo_locations import *

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

        ipv6 = get_ipv6_address(domain)
        domain_dict[domain]["ipv6_addresses"] = ipv6

        http_server = get_http_server(domain)
        domain_dict[domain]["http_server"] = http_server

        insecure = get_insecure(domain)
        domain_dict[domain]["insecure_http"] = insecure

        redirect = get_redirect(domain)
        domain_dict[domain]["redirect_to_https"] = redirect

        ssl = check_ssl(domain)
        tls = check_tls(domain)
        finaltls = ssl + tls
        domain_dict[domain]["tls_versions"] = finaltls

        rootca = check_root(domain)
        domain_dict[domain]["root_ca"] = rootca
        
        hsts = get_hsts(domain)
        domain_dict[domain]["hsts"] = hsts

        rdns = get_rdns(ipv4)
        domain_dict[domain]["rdns"] = rdns

        rtt = get_rtt_range(ipv4)
        domain_dict[domain]["rtt_range"] = rtt

        locations = get_locations(ipv4)
        domain_dict[domain]["geo_locations"] = locations
        

out_file = open(output_file, "w")
json.dump(domain_dict, out_file, sort_keys=False, indent=4)
out_file.close()
