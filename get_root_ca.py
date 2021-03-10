import sys
import socket
import OpenSSL
# import ssl
from OpenSSL import SSL
import subprocess

def check_root(domain):
    url = domain + ":443"
    try:
        root = subprocess.check_output(["openssl", "s_client", "-connect", url], input=b'',
              timeout=2, stderr=subprocess.STDOUT).decode("utf-8")

        root = root.split('\n')
        root = root[0]
        root = root.replace(',', '=')
        root = root.split('=')

        for i in range(len(root)):
            if ' O ' in root[i]:
                root_ca = root[i+1]

        root_ca = root_ca.lstrip()
        return root_ca


    except subprocess.TimeoutExpired as err:
        print("Timer expired")
        pass

    except:
        return None
