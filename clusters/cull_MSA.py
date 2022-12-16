#! /usr/local/bin/python
#This code was used to remove gappy sequences from MSAs

import sys, string
import numpy as np
 
def read_MSA(f):

    s = ''

    seqs = []

    IDs  = []

    for i in range(len(f)):

        if f[i][0] == '>':

            IDs.append(f[i])

            if s:

                seqs.append(s)

                s = ''
        else:

            s += f[i]

    seqs.append(s)

    return seqs, IDs

 

def sequence_matrix(seqs):

 

    seq_mat = []

 

    for seq in seqs:

 

        line = []

 

        for l in seq:

 

            if l != '-':

                line.append(1)

            else:

                line.append(0)

 

        seq_mat.append(line)

 

    seq_mat = np.matrix(seq_mat)

 

    return seq_mat

 

def get_column_averages(seq_mat,l):

 

    averages = []

 

    for i in range(l):

 

        averages.append(np.mean(seq_mat[:,i]))

 

    return averages

 

def find_sparse_zones(averages):

 

    sparse_zones = []

 

    l = 0

    sparse_hit = 0

    sidx = 0

 

    for i in range(len(averages)):

 

        if averages[i] < 0.05:

            if not sparse_hit:

                l = 1

                sidx = i

                sparse_hit = 1

 

            else:

                l +=1

 

        else:

 

            if sparse_hit and l >= 8:

                sparse_zones.append((sidx,sidx+l))

 

            sparse_hit = 0

            l = 0

           

    if sparse_hit and l >= 8:

        sparse_zones.append((sidx,sidx+l))

 

    return sparse_zones

 

def find_pop_zones(averages):

 

    l2 = 0

    pop_hit = 0

    pidx = 0

 

    pop_zones = []

 

    for i in range(len(averages)):

 

        if averages[i] >= 0.9:

            if not pop_hit:

                l2 = 1

                pidx = i

                pop_hit = 1

 

            else:

                l2 +=1

 

        else:

 

            if pop_hit and l2 >= 10:

                pop_zones.append((pidx,pidx+l2))

 

            pop_hit = 0

            l2 = 0

           

    if pop_hit and l2 >= 10:

        pop_zones.append((sidx,sidx+l))

 

    return pop_zones

 

#Included seqs as an input to this program because while importing this function into the cull_files_from_folders program, need this input

#seqs is a global variable in the culling program

def find_anomylous_sequences(seq_mat,sparse_zones,pop_zones,seqs):

 

    bad_idxs = []

 

    for z in sparse_zones:

 

        m =  seq_mat[:,z[0]:z[1]]

 

        for i in range(len(seqs)):

            if np.mean(m[i]) >= 0.1:

                bad_idxs.append(i)

 

 

    for p in pop_zones:

 

        m2 = seq_mat[:,p[0]:p[1]]

 

        for i in range(len(seqs)):

            if np.mean(m2[i]) < 0.1:

                bad_idxs.append(i)

 

    return bad_idxs

 

#fw is a global variable in the culling program, but needs to be given as an input when the function is imported

def print_good_seqs(seqs,IDs,anomylous_seqs,fw):

    #counter to count the number of sequences in the program

    counter = 0

    for i in range(len(seqs)):

 

        if i not in anomylous_seqs:

            fw.write(IDs[i]+"\n")

            #print string.join([x for x in seqs[i] if x != '-'],'')

            fw.write(seqs[i]+"\n")

            #comment 'print seqs[i]' and uncomment the 'string.join' line to see

            #dealigned sequences instead of aligned

            counter += 1

    return counter

if __name__ == '__main__':

    f = open(sys.argv[1]).read().splitlines()

    #Read in MSA
    fw= open(sys.argv[2],'w')
    seqs,IDs = read_MSA(f)

    #Matrix of all sequences.  All positions with gaps are '0' all other positions are '1'
    seq_mat = sequence_matrix(seqs)

    
    #Average all columns in the matrix to determine which regions of the alignment are
    #highly and sparsely populated
    averages = get_column_averages(seq_mat,len(seqs[0]))

    #Find regions with at least 8 consecutive AAs in which at least 95% of the sequences
    #have gaps 
    sparse_zones = find_sparse_zones(averages)

    print sparse_zones


    #Find regions with at least 10 consecutive AAs in which at least 90% of the sequences
    #do not have gaps
    populated_zones = find_pop_zones(averages)

    print populated_zones

    #staggers = find_staggers(averages)

    #print seqs[0][190:199]

    #print staggers

    #sys.exit()

    anomylous_seqs  = find_anomylous_sequences(seq_mat,sparse_zones,populated_zones,seqs)

    print_good_seqs(seqs,IDs,anomylous_seqs,fw)
    fw.close()
