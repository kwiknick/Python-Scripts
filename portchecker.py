#!/usr/bin/python

import socket, sys, getopt

def main(argv):
    port = 80
    ipaddress = '127.0.0.1'
    try:
        opts, args = getopt.getopt(argv, "hpa",["port=","ip="])
    except getopt.GetoptError:
        print 'portchecker.py -port <portnumber> -ip <ipaddress>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'portchecker.py -port <portnumber> -ip <ipaddress>'
            sys.exit()
        elif opt in ("-p", "--port"):
            port = int(arg)
        elif opt in ("-a", "--ip"):
            ipaddress = arg
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((ipaddress, port))
    ipaddressstring = str(ipaddress)
    portstring = str(port)
    if result == 0:
        print "Port " + portstring + " is open for ipaddress " + ipaddressstring
    else:
        print "Port " + portstring + " is not open for ipaddress " + ipaddressstring

if __name__ == "__main__":
    main(sys.argv[1:])

