#! /usr/local/bin/python

import sys, string
from Bio import pairwise2

def tru_len(s):
    return len([x for x in s if x != '-'])

def get_seqs(f):

    i = 0

    seqs = []
    ids  = []

    while i < len(f):

        if f[i][0] == '>':
            ids.append(f[i])
            seqs.append(f[i+1])
            i += 2

        else:
            print 'Indexing error!'
            i += 1

    return seqs, ids

def cluster_seqs(cseqs,rseqs,cids):

    for i in xrange(len(cseqs)):

        max_idx = -999
        max_ID  = 0

        for j in xrange(len(rseqs)):

            a = pairwise2.align.localxs(cseqs[i],rseqs[j],-1,-0.5)
            #print a[0]
            #print a[0][2]/min(tru_len(cseqs[i]),tru_len(rseqs[j]))
            if a[0][2]/min(tru_len(cseqs[i]),tru_len(rseqs[j])) >= 0.64:
                max_idx = j
                max_ID = a[0][2]/min(tru_len(cseqs[i]),tru_len(rseqs[j]))
                break

            if a[0][2]/min(tru_len(cseqs[i]),tru_len(rseqs[j])) > max_ID:
                max_idx = j
                max_ID = a[0][2]/min(tru_len(cseqs[i]),tru_len(rseqs[j]))

        print '%-30s %-3i %-3.5f' %(cids[i],max_idx,max_ID)
        print cseqs[i]


if __name__ == '__main__':

    f = open(sys.argv[1]).read().splitlines()
    f2 = open(sys.argv[2]).read().splitlines()

    check_seqs = []
    check_ids = []
    ref_seqs = []
    ref_ids  = []
    unique_seqs = []

    check_seqs,check_ids = get_seqs(f)
    ref_seqs,ref_ids = get_seqs(f2)

    cluster_seqs(check_seqs,ref_seqs,check_ids)

                    
                
                
