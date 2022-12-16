#! /usr/local/bin/python

import sys

if __name__ == '__main__':

    f = open(sys.argv[1]).read().splitlines()

    i = 0

    while i < len(f):

        if f[i][0:3] == '==>':
            if f[i+1][0] == '>':
                print f[i].split()[1], f[i+1].split()[0]
            elif f[i+2][0] == '>':
                print f[i].split()[1], f[i+2].split()[0]
            else:
                print 'Error!'
            i += 3
