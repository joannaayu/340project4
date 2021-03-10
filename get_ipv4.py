import subprocess
import sys

def get_ipv4_address(domain):
    result = subprocess.check_output(["nslookup", "-type=A", domain, "8.8.8.8"] ,
          timeout=2, stderr=subprocess.STDOUT).decode("utf-8")


    result = result.replace(' ', '')
    result = result.replace('\t', '')
    result = result.replace('\n', ':')
    result = result.split(':')
    # print(result)

    result.pop(0)
    result.pop(0)
    result.pop(0)
    result.pop(0)

    new_results_array = []

    for i in range(len(result)):
        if i == 0:
            continue

        elif result[i-1] == 'Address':
            new_results_array.append(result[i])

    # print(new_results_array)

    return new_results_array
