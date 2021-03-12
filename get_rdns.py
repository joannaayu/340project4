import os
import sys
import socket

def get_rdns(ipv4):
    rdns_arr = []

    for ip in ipv4:
        try:
            rdns = socket.gethostbyaddr(ip)
            print("rdns", rdns)
            rdns_name = rdns[0]
            # rdns_name2 = rdns[1][0]
            rdns_arr.append(rdns_name)
            # rdns_arr.append(rdns_name2)

            if len(rdns[1]) != 1:
                other_rdns = rdns[1]
                del other_rdns[0]
                print("othere_rdns", other_rdns)
                for r in range(len(other_rdns)):
                    rdns_arr.append(other_rdns[r])


            rdns_arr = list(set(rdns_arr))


        except socket.herror:
            pass

    print("final dns", rdns_arr)
    return rdns_arr
