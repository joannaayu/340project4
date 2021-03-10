import subprocess
import sys
import re

def get_ipv4_address(domain):

    try:
        result = subprocess.check_output(["nslookup", "-type=A", domain, "8.8.8.8"], timeout=2, stderr=subprocess.STDOUT).decode("utf-8")
        result = result.split("\n")
        ipv4_array = []

        for i in range(len(result)):
            if "Address" in result[i]:
                remove = "Address" + ":" + " "
                ipv4 = re.sub(remove, "", result[i])
                ipv4_array.append(ipv4)

        del ipv4_array[0]

    except:
        print("Timeout error!")
        pass

    return ipv4_array
