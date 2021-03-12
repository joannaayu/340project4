import requests
import json

def get_hsts(domain):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}
    url = f"http://{domain}/"
    hsts = False

    try:
        response = requests.head(url, timeout=5, headers=headers)
        headers = response.headers

        if 'Location' not in headers:
            hsts = False

        if 'Strict-Transport-Security' in headers:
            hsts = True

        else:
            count = 1
            while count < 10:
                if 'Location' in headers:
                    redirect_url = response.headers['Location']
                    re_url = requests.get(redirect_url)
                    redirect_response = requests.head(re_url.url, timeout=5)

                    if 'Strict-Transport-Security' in redirect_response.headers:
                        hsts = True
                        break

                    headers = redirect_response
                    count = count + 1

                else:
                    if 'Strict-Transport-Security' in headers:
                        hsts = True
                        break
                    else:
                        hsts = False
                        break


    except requests.Timeout:
        hsts = False
        print("Timeout occured when getting HSTS")
        pass

    except:
        #if we are unable to send the request at all
        hsts = False
        print("Could not send GET request for HSTS")
        pass


    return hsts
