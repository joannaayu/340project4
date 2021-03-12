import time
import socket
import subprocess
import shlex


def get_rtt_range(ipv4):
    rtt_arr = []

    for ip in ipv4:
        worked = False
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            port = 80
            ip_addr = ip
            check = sock.connect_ex((ip_addr, port))

            if check == 0:
                worked = True
                start = time.time()
                sock.sendall(b'1')
                data = sock.recv(1)
                finish = time.time()
                rtt = finish-start
                rtt_arr.append(rtt)
                sock.close()

            else:
                sock.close()
                print("Socket timed out on port 80")
                pass

        except socket.timeout:
            sock.close()
            pass

        except:
            sock.close()
            pass

        finally:
            sock.close()
            pass

        try:
            if worked == False:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                port = 443
                ip_addr = ip
                check = sock.connect_ex((ip_addr, port))

                if check == 0:
                    worked = True
                    # sock.settimeout(3)
                    # sock.connect((ip_addr, 443))
                    start = time.time()
                    sock.sendall(b'1')
                    data = sock.recv(1)
                    finish = time.time()
                    rtt = finish-start
                    rtt_arr.append(rtt)
                    sock.close()

                else:
                    sock.close()
                    print("Socket timed out on port 443")
                    pass

        except socket.timeout:
            sock.close()
            pass

        except:
            sock.close()
            pass

        finally:
            sock.close()
            pass

        try:
            if worked == False:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                port = 22
                ip_addr = ip
                check = sock.connect_ex((ip_addr, port))

                if check == 0:
                    worked == True
                    # sock.settimeout(3)
                    # sock.connect((ip_addr, 22))
                    start = time.time()
                    sock.sendall(b'1')
                    data = sock.recv(1)
                    finish = time.time()
                    rtt = finish-start
                    rtt_arr.append(rtt)
                    sock.close()

                else:
                    sock.close()
                    print("Socket timed out on port 22")
                    pass

        except socket.timeout:
            sock.close()
            pass

        except:
            sock.close()
            pass

        finally:
            sock.close()
            pass

    if len(rtt_arr) == 0:
        return None
    elif len(rtt_arr) == 1:
        final_arr = rtt_arr
    else:
        max_val = max(rtt_arr)
        min_val = min(rtt_arr)

        final_arr = [min_val, max_val]

    return final_arr
