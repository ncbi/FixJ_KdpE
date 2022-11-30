"""
After inferring rooting using IQ-TREE2
please refer to http://www.iqtree.org/doc/Rootstrap for more info

The output log file generated is analyzed to get rooting info
and to plot FigS5

Usage: python3.8 getvalues_CheckRooting.py

"""
from pathlib import Path
import re
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import seaborn as sns

sns.set( rc = { 'axes.labelsize' : 20 })
sns.set_style(style='white')

# set Path and folders, files
# change these to your local paths before running them
main_dir = Path("/Users/chakravartyd2/FixJ_KdpE/")
data_dir = main_dir / "data"
inputfile = data_dir / "root_test.iqtree"
outfile = data_dir / "root_test.csv"

# set pattern for regular expression
pattern = re.compile(r"^\s*\d+\s+-?\d+[.]?\d+\s+-?\d*[.]?\d*")

# create filehandle for writing
# write the header
Fout = open(outfile, 'w')
header = "Tree,logL,deltaL,bp-RELL,p-KH,p-SH,c-ELW,p-AU\n"
Fout.write(header)

# create empty lists for trees and their p-values
trees = []
pvals = []

# go through the input file
# get info on each tree and save in output
with open(inputfile,'r') as Infile:
    for line in Infile:
        line=line.strip()
        m = pattern.search(line)
        if  m:
            tree, rest = line.split(' ', maxsplit=1)
            logL = float(rest[:12])
            deltaL = float(rest[12:21])
            bpRELL = float(rest[21:29])
            pKH = float(rest[30:38])
            pSH = float(rest[39:47])
            cELW = float(rest[48:59])
            pAU = float(rest[60:70])
            
			# we will use this to plot the distribution
            pvals.append(pAU)
            
			# goes in the output file
            outline = f"{tree},{logL},{deltaL},{bpRELL},{pKH},{pSH},{cELW},{pAU}\n"
            Fout.write(outline)

Fout.close()

# convert the array to a numpy array for plotting
pval_np = np.array(pvals)
size = pval_np.size
sorted_pval = np.sort(pval_np)
ranks_array = np.arange(1, size+1, 1)

# create files to save plots

filename = main_dir / "plots" / "FigS5.pdf"

# plot and save the figures

fig1 = plt.figure()
p = sns.histplot(sorted_pval, bins=25, kde=True)
p.set_xlabel("pAU", fontsize = 20)
p.set_ylabel("Frequency", fontsize = 20)

fig2 = plt.figure()
plt.scatter(sorted_pval, ranks_array, c ="blue")
plt.xlabel("pAU", fontsize = 20)
plt.ylabel("rank", fontsize = 20)

def save_multi_image(filename):
   pp = PdfPages(filename)
   fig_nums = plt.get_fignums()
   figs = [plt.figure(n) for n in fig_nums]
   for fig in figs:
      fig.savefig(pp, format='pdf')
   pp.close()

save_multi_image(filename)
