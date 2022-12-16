#! /usr/local/bin/python

import sys

if __name__ == '__main__':

    f = open(sys.argv[1]).read().splitlines()

    i = 0

    clusters = []

    found_EOCs = 0
    found_BOCs = 0

    while not found_EOCs:

        if f[i] == 'producing':
            found_BOCs = 1
            i += 2
            continue

        if found_BOCs and not f[i]:
            found_EOCs = 1

        elif found_BOCs:

            if f[i] not in clusters:
                clusters.append(f[i])

        i += 1
    
    print clusters

        
