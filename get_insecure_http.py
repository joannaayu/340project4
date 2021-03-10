import requests
import json

def get_insecure(domain):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}
    url = f"http://{domain}/"
    r = requests.get(url)
    #print(r.url)
    #print(url)
    #url = "http://www.usnews.com"

    try:
        response = requests.head(url, timeout=5, headers=headers)
        # print(response.status_code)
        # print(response.headers)

        if 301 == response.status_code or 302 == response.status_code or 200 == response.status_code:
            insecure = True

        # elif 308 == response.status_code or 301 == response.status_code and "https" in response.headers["location"]:
        #     insecure = False
        #     redirect = True

        else:
            insecure = False

    except requests.Timeout:
        print("Timeout occured, trying again")
        pass

    return insecure


# import sys
# import socket
#
# #Taken from https://www.geeksforgeeks.org/port-scanner-using-python/
#
# def get_insecure_http(ipv4):
#
#     target = ipv4
#     port = 80
#
#     try:
#         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         socket.setdefaulttimeout(1)
#
#         # returns an error indicator
#         result = s.connect_ex((target,port))
#         if result == 0:
#             s.close()
#             return True
#         else:
#             s.close()
#             return False
#
#
#     except KeyboardInterrupt:
#             print("\n Exitting Program !!!!")
#             return(False)
#             sys.exit()
#     except socket.gaierror:
#             print("\n Hostname Could Not Be Resolved !!!!")
#             return(False)
#             sys.exit()
#     except socket.error:
#             print("\ Server not responding !!!!")
#             return(False)
#             sys.exit()
