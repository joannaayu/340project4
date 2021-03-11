import requests
import json

def get_insecure(domain):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
    url = f"http://{domain}/"
    r = requests.get(url)
    #print(r.url)
    #print(url)
    #url = "http://www.usnews.com"

    try:
        response = requests.head(url, timeout=5, headers=headers)
        # print(response.status_code)
        # print(response.headers)

        insecure = True

        # elif 308 == response.status_code or 301 == response.status_code and "https" in response.headers["location"]:
        #     insecure = False
        #     redirect = True

    except requests.Timeout:
        insecure = False
        print("Timeout occured, trying again")
        pass

    except:
        insecure = False
        print("other error occured!")


    return insecure


# import sys
# import socket

#Taken from https://www.geeksforgeeks.org/port-scanner-using-python/

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
