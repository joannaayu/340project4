import subprocess
import sys
import re

def get_ipv4_address(domain):
<<<<<<< HEAD
    ipv4_array = []

=======
>>>>>>> d42984b6be1e740ce1c0f5929ce33c32b71579f9
    try:
        result = subprocess.check_output(["nslookup", "-type=A", domain, "8.8.8.8"], timeout=2, stderr=subprocess.STDOUT).decode("utf-8")
        result = result.split("\n")

        for i in range(len(result)):
            if "Address" in result[i]:
                remove = "Address" + ":" + " "
                ipv4 = re.sub(remove, "", result[i])
                ipv4_array.append(ipv4)

        del ipv4_array[0]

    except subprocess.TimeoutExpired:
        print("Timeout error when getting IPV4")
        pass

    except:
        print("Unable to perform nslookup for IPV4")
        pass

    return ipv4_array

    # result = subprocess.check_output(["nslookup", "-type=A", domain, "8.8.8.8"] ,
    #       timeout=2, stderr=subprocess.STDOUT).decode("utf-8")
    # result = result.replace(' ', '')
    # result = result.replace('\t', '')
    # result = result.replace('\n', ':')
    # result = result.split(':')
    # # print(result)
    #
    # result.pop(0)
    # result.pop(0)
    # result.pop(0)
    # result.pop(0)
    #
    # new_results_array = []
    #
    # for i in range(len(result)):
    #     if i == 0:
    #         continue
    #
    #     elif result[i-1] == 'Address':
    #         new_results_array.append(result[i])
    #
    # # print(new_results_array)
    #
    # return new_results_array
