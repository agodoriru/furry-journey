#! /usr/bin/env python
# -*- coding:utf-8 -*-

import argparse
import getopt
import socket
import sys

import crypt as cr
import radix_translation as rad_trans
import IP_translation as IP

target = ''
port = 0


def main():

    if not len(sys.argv[1:]):
        usage()

    global port
    global target

    parser = argparse.ArgumentParser(
        description='python network tool',
        prog='prog.py',
        usage='',
        epilog='',

    )

    parser.add_argument('-p', '--port', dest='port',  type=int, action='store', help='port number')
    parser.add_argument('-t', '--target', type=str, help='target hostname or IP address')
    parser.add_argument('-c', '--command', dest='command', type=str)
    parser.add_argument('-n', '--number', dest='number', type=int)
    parser.add_argument('-st', '--string', dest='string', type=str)
    parser.add_argument('-v', '--version', action='version', version='Version 1.0.0', help='show version')

    args = parser.parse_args()

    if args.command == 'list':
        port_check_list(args.target)

    if args.command == 'encmd5':
        print cr.md5_encrypt(args.string)

    if args.command == '10to2':
        rad_trans.from10to2(args.number)

    if args.command == 'IP':
        IP.IP_translation()


    #print("HOGE")


### port OPEN or CLOSE
def port_check(target, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port_check_flag = client.connect_ex((target, port))
    client.close()

    if port_check_flag == 0:
        print("[*] target:%s port: %d OPEN" % (target, port))
    else:
        print("[*] target:%s port: %d CLOSE" % (target, port))

    sys.exit(0)


# arg start_port end_port target_host
def port_check_list(target):
    print("***********************************")
    print("         [*]target : %s        " % target)
    print("***********************************")
    start_port=0
    end_port=56635

    for i in range(start_port, end_port+1):
        #port_check_flag=0
        client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port_check_flag=client.connect_ex((target,i))
        client.close()

        if port_check_flag==0:
            print("[*] port: %d/TCP OPEN" % i)


    print("Done")


    sys.exit(0)






def check_args():
    print(args)



def usage():
    print("will write USAGE")
    sys.exit(0)



main()
