import sys
import socket

#Taken from https://www.geeksforgeeks.org/port-scanner-using-python/

def get_insecure_http(ipv4):

    target = ipv4
    port = 80

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        # returns an error indicator
        result = s.connect_ex((target,port))
        if result == 0:
            s.close()
            return True
        else:
            s.close()
            return False


    except KeyboardInterrupt:
            print("\n Exitting Program !!!!")
            return(False)
            sys.exit()
    except socket.gaierror:
            print("\n Hostname Could Not Be Resolved !!!!")
            return(False)
            sys.exit()
    except socket.error:
            print("\ Server not responding !!!!")
            return(False)
            sys.exit()
