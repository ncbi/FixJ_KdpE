"""
Get all the trees with pAU > 0.8
save details in an output file

"""
from pathlib import Path

# set Path and folders, files
main_dir = Path("/Users/chakravartyd2/FixJ_KdpE/")
data_dir = main_dir / "data"
inputfile = data_dir / "root_test.csv"
outputfile = data_dir / "trees_of_interest.csv"

# create filehandle for writing
# write the header

OF = open(outputfile,'w')
header = "#Tree,pAU,pKH\n"
OF.write(header)

# go through the input file
# find the trees of interest, pAU > 0.8
# save details in the output file

with open(inputfile,'r') as Infile:
    for line in Infile:
        line = line.strip()
        if line.startswith("Tree"): # skip Header
            continue
        # split the line by commas
        lst_var = line.split(",")
        
        if float(lst_var[7]) > 0.8: # check for pAU > 0.8
        	# pAU, p-value of approximately unbiased (AU) test (Shimodaira, 2002)
            pvalue = round(float(lst_var[7]),2)
            # pKH, p-value of one sided Kishino-Hasegawa test (1989)
            pkh = round(float(lst_var[4]),2)
            outline = "tree" + str(lst_var[0])+ "," + str(pvalue)+ "," + str(pkh) + "\n"
            OF.write(outline)

OF.close()


