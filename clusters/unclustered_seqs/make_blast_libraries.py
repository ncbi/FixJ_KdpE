#! /usr/local/bin/python

import sys, string

if __name__ == '__main__':

    ns = string.split(sys.argv[1],',')

    ns = [int(x) for x in ns]

    print '#! /bin/bash'
    print ''

    for i in xrange(len(ns)):

        nums = ns[0:i]+ns[i+1:len(ns)]

        print 'cat '+'cluster%i_cleaned_24.txt '*len(nums) %tuple(nums) +'> cluster_m%i.txt' %(ns[i])

        print 'makeblastdb -in cluster_m%i.txt -dbtype prot -out /home/porterll/evolved_fs_analysis/mega_clusters_full/blastdbs/cluster_m%i' %(ns[i],ns[i])

        print ''
