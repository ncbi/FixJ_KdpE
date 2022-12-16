#! /usr/local/bin/python

import sys

if __name__ == '__main__':

    f = open(sys.argv[1]).read().splitlines()

    i = 0

    while i < len(f):

        info = f[i].split()[0][1:]

        of = open('cluster366_fullseqs90/'+info+'.fa','w')

        of.write(f[i]+'\n')
        of.write(f[i+1]+'\n')

        i += 2

        
