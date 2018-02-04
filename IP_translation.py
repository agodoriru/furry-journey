#! /usr/bin/env python
# -*- coding:utf-8 -*-


def IP_translation():

    print 'input_IP_address'

    IP = raw_input()

    IP_arr=IP.split(".")

    for i in IP_arr:

        print (i,)
        bin_i=format(str(i), '08b')
        print bin_i






