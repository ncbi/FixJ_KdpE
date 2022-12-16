#! /usr/local/bin/python

import sys, string

DIR='fixJ_kdpe_seqs2/'

if __name__ == '__main__':

    f = open(sys.argv[1]).read().splitlines()

    for i in f:

        ofn = string.split(i,'.')[0]+'_clusters.txt'

        print './cross_identities.py %s fixJ_kdpE_seqs_0t290_24.txt > %s' %(i,ofn)
