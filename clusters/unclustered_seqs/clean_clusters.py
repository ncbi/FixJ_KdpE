#! /usr/local/bin/python

import sys

if __name__ == '__main__':

    fns = open(sys.argv[1]).read().splitlines()

    l35 = open('less_than_24.txt','w')
    shr = open('too_short.txt','w')

    for fn in fns:

        f = open(fn).read().splitlines()

        of = open(fn[:-4]+'_cleaned_24.txt','w')

        for i in xrange(len(f)):

            info = f[i].split()

            if info[0][0] == '>' and float(info[2]) < 0.24:
                l35.write(f[i]+'\n')
                l35.write(f[i+1]+'\n')

            elif info[0][0] == '>' and i+1 < len(f) and len(f[i+1]) < 162:
                shr.write(f[i]+'\n')
                shr.write(f[i+1]+'\n')

            if info[0][0] == '>' and float(info[2]) >=0.24:
                if i+1 < len(f) and len(f[i+1]) >= 162:
                    of.write(f[i] + '\n')
                    of.write(f[i+1] + '\n')

        of.close()
 
            
