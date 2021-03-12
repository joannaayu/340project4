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
                # sock.settimeout(3)
                # sock.connect((ip_addr, 80))
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



    #
    #     sock_params = ("104.244.42.129", 80)
    # with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    #     try:
    #         sock.settimeout(30)
    #         sock.connect(sock_params)
    #         start = time.time()
    #         sock.sendall(b'1')
    #         data = sock.recv(1)
    #         finish = time.time()
    #         rtt = finish-start
    #         rtt_arr.append(rtt)
    #         sock.close()
    #
    #     except socket.timeout:
    #         sock.close()
    #         print("Socket timed out on port 80")
    #
    # sock_params = ("104.244.42.129", 443)
    # with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    #     try:
    #         sock.settimeout(30)
    #         sock.connect(sock_params)
    #         start = time.time()
    #         sock.sendall(b'1')
    #         data = sock.recv(1)
    #         finish = time.time()
    #         rtt = finish-start
    #         rtt_arr.append(rtt)
    #         sock.close()
    #
    #     except  socket.timeout:
    #         sock.close()
    #         print("Socket timed out on port 443")
    #
    # sock_params = ("104.244.42.129", 22)
    # with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    #     try:
    #         sock.settimeout(30)
    #         sock.connect(sock_params)
    #         start = time.time()
    #         sock.sendall(b'1')
    #         data = sock.recv(1)
    #         finish = time.time()
    #         rtt = finish-start
    #         rtt_arr.append(rtt)
    #         sock.close()
    #
    #     except  socket.timeout:
    #         sock.close()
    #         print("Socket timed out on port 22")


    #sh -c "time echo -e '\x1dclose\x0d' | telnet 172.217.6.110 443"
    # for ip_addr in ipv4:
    #     command = "sh -c time echo -e '\x1dclose\x0d' | telnet " + ip_addr
    #     s_cmd = shlex.split(command)
    #     print(s_cmd)
    #     #
    #     output = subprocess.check_output(s_cmd, shell=True, timeout=5, stderr=subprocess.STDOUT).decode("utf-8")
    #     #output = output.decode("utf-8")
    #     # output = subprocess.check_output(["sh", "-c", cmd],
    #     #     timeout=5, stderr=subprocess.STDOUT).decode("utf-8")
    #     print(ip_addr)
    #     # ps = subprocess.Popen(cmd, shell=, stdout = subprocess.PIPE)
    #     # output = subprocess.check_output(('sh', '-c', cmd), stdin = ps.stdout).decode("utf-8")
    #     # ps.wait()
    #     #output = ps.communicate()
    #     print(output)
