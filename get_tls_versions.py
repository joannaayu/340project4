import sys
import socket
import OpenSSL
# import ssl
from OpenSSL import SSL
import subprocess


# code taken from https://stackoverflow.com/questions/63214304/how-to-check-a-website-for-sslv2-or-sslv3

def check_ssl(domain):
    ssltable = []
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        osobj = SSL.Context(SSL.SSLv23_METHOD)
        osobj.set_options(OpenSSL.SSL.OP_NO_TLSv1 | OpenSSL.SSL.OP_NO_TLSv1_1 | OpenSSL.SSL.OP_NO_TLSv1_2 | OpenSSL.SSL.OP_NO_TLSv1_3)
        sock.connect((domain, int(443)))
        oscon = SSL.Connection(osobj, sock)
        oscon.set_connect_state()

        try:
            oscon.do_handshake()
            ssltable.append("SSLv2")
            ssltable.append("SSLv3")
            return ssltable

        except OpenSSL.SSL.Error as err:
            if err.args[0][0][2] == "no protocols available":
                # print("no ssl23")
                return ssltable
    except:
        # print("port closed")
        return ssltable

# def check_ssl3(domain):
#
#     ssltable = []
#
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     osobj = SSL.Context(SSL.SSLv3_METHOD)
#     osobj.set_options(OpenSSL.SSL.OP_NO_TLSv1 | OpenSSL.SSL.OP_NO_TLSv1_1 | OpenSSL.SSL.OP_NO_TLSv1_2 | OpenSSL.SSL.OP_NO_TLSv1_3)
#     sock.connect((domain, int(443)))
#     oscon = SSL.Connection(osobj, sock)
#     oscon.set_connect_state()
#
#     try:
#         oscon.do_handshake()
#         ssltable.append("SSLv3")
#         return ssltable
#
#     except OpenSSL.SSL.Error as err:
#         if err.args[0][0][2] == "no protocols available":
#             return ssltable

def check_tls(domain):
    url = domain + ":443"

    tlstable = []
    try:

        tls1_0 = subprocess.check_output(["openssl", "s_client", "-tls1", "-connect", url], input=b'',
              timeout=2, stderr=subprocess.STDOUT).decode("utf-8")

        if "BEGIN CERTIFICATE" in tls1_0:
            tlstable.append("TLSv1.0")
    except:
        # print('no tls1.0')
        pass

    try:
        tls1_1 = subprocess.check_output(["openssl", "s_client", "-tls1_1", "-connect", url], input=b'',
              timeout=2, stderr=subprocess.STDOUT).decode("utf-8")

        if "BEGIN CERTIFICATE" in tls1_1:
            tlstable.append("TLSv1.1")
    except:
        # print('no tls1.1')
        pass

    try:
        tls1_2 = subprocess.check_output(["openssl", "s_client", "-tls1_2", "-connect", url], input=b'',
              timeout=2, stderr=subprocess.STDOUT).decode("utf-8")

        if "BEGIN CERTIFICATE" in tls1_2:
            tlstable.append("TLSv1.2")
    except:
        # print('no tls1.2')
        pass

    try:
        tls1_3 = subprocess.check_output(["openssl", "s_client", "-tls1_3", "-connect", url], input=b'',
              timeout=2, stderr=subprocess.STDOUT).decode("utf-8")

        if "BEGIN CERTIFICATE" in tls1_3:
            tlstable.append("TLSv1.3")
    except:
        # print('no tls1.3')
        pass

    return tlstable
