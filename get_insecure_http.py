import requests
import json

def get_insecure(domain):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
    url = f"http://{domain}/"
    # r = requests.get(url)

    try:
        response = requests.head(url, timeout=5, headers=headers)
        insecure = True

    except requests.Timeout:
        insecure = False
        print("Timeout occured in insecure")
        insecure = False
        pass

    except:
        insecure = False
        print("did not connect on port 80, not insecure!")
        pass

    return insecure
