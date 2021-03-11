import os
import sys
import socket

def get_rdns(ipv4):
    rdns_arr = []
    # google = socket.gethostbyaddr("172.217.6.110")
    # print(google)

    for ip in ipv4:
        try:
            rdns = socket.gethostbyaddr(ip)
            rdns_name = rdns[0]
            rdns_arr.append(rdns_name)

            # print("IP:", ip)
            # print("RDNS ARR:", rdns)
            # print("RDNS NAME:", rdns_name)

            if len(rdns[1]) != 1:
                other_rdns = rdns[1]
                #del other_rdns[0]
                print(other_rdns)
                for r in range(len(other_rdns)):
                    if other_rdns[r] not in rdns_arr:
                        rdns_arr.append(other_rdns[r])


        except socket.herror:
            print("Socket error, unknown host")
            pass


    return rdns_arr
