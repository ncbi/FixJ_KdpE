#! /usr/local/bin/python

import sys, string

if __name__ == '__main__':

    f = open(sys.argv[1]).read().splitlines()

    for i in f:

        fa = open(i).read().splitlines()

        num = string.split(i,'_')[4]

        of = open('seqs_joined_%s.txt' %(num),'w')

        for j in xrange(len(fa)):
            
            if j < len(fa) - 2:
                of.write(fa[j]+'\n')

            elif j == len(fa) - 2:
                if fa[j][0] == '>':
                    break
                else:
                    of.write(fa[j]+'\n')

            else:
                break

 

        n2 = string.split(i,'_clusters')[0]+'_unfinished_clusters.txt'

        fb = open(n2).read().splitlines()

        for k in xrange(len(fb)):
            of.write(fb[k]+'\n')

        of.close()
