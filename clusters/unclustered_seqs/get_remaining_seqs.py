#! /usr/local/bin/python

import sys, string

if __name__ == '__main__':

    f = open(sys.argv[1]).read().splitlines()

    for i in f:

        info = i.split()

        n = string.split(info[0],'_clusters')[0]

        f2 = open(n+'.txt').read().splitlines()

        eod_found = 0

        print n+'.txt'

        of = open(n+'_unfinished.txt','w')

        for j in f2:
            
            if j == info[1]:
                eod_found = 1

            if eod_found:
                of.write(j+'\n')


        of.close()

        
