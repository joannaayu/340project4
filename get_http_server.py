import requests
import json

def get_http_server(domain):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}
    url = f"http://{domain}/"
    r = requests.get(url)
    #print(r.url)
    # print(url)
    #url = "http://www.usnews.com"

    try:
        response = requests.head(url, timeout=5, headers=headers)
        # print(response.history)
        # print(response)
        # print(response.headers)
        if 'Server' in response.headers:
            server = response.headers["Server"]
            http_server = server
        else:
            http_server = None

    except requests.Timeout:
        print("Timeout occured, trying again")
        pass

        # response = requests.head(r.url)
        #
        # if 'Server' in response.headers:
        #     server = response.headers["Server"]
        #     http_server = server
        # else:
        #     http_server = None


    #print(http_server)

    return http_server
