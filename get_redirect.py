import requests
import json

def get_redirect(domain):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}
    url = f"http://{domain}/"
    count = 0
    return redirect(url, 0)

def redirect(url, counter):

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}

    if counter == 10:
        return False


    try:
        response = requests.head(url, timeout=5, headers=headers)

        if 300 <= response.status_code < 310:
                if "https" in response.headers["location"]:
                    return True

                else:
                    return redirect(response.headers["location"], (counter + 1))

        else:
            return False



    except requests.Timeout:
        print("Timeout occured when getting redirect")
        pass

    except:
        #unable to send requests to redirects
        print("Failed to send GET request for redirect")
        pass
