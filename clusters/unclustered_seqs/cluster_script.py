#! /usr/local/bin/python

import sys 

if __name__ == '__main__':

    n = int(sys.argv[1])

    for i in xrange(n):

        print ("grep ' %i ' -A 1 all_clusters.txt > cluster%i.txt" %(i,i))
