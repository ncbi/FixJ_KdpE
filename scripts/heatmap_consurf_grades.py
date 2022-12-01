"""
Create HeatMap for the ConSurf grades
going from 1 (variable) to 9 (conserved)

Refer to https://consurf.tau.ac.il/consurf_index.php 
for details

Comparing if different phylogenetic trees 
are given as input, does the ConSurf grades differ?

Comparing if different MSA profiles (including all, only HTH or wH)
are given as input, does the ConSurf grades differ?

Usage: python3.8 heatmap_consurf_grades.py

"""

from pathlib import Path
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(font_scale=1.5)

def plot_heatmap(list_files,col_names,output):
	"""
	Convert the data to Pandas dataframe
	Use SeaBorn to plot the HeatMap
	
	Input parameters: 
	list <- files of ConSurf grades
	col_names <- list of column names
	output <- filepath to save the figure
	
	"""
	data_dict = {}
	for file in list_files:
		filepath = data_dir / file
		with open(filepath, 'r') as InFile:
			for line in InFile:
				(pos,score) = line.strip().split()
				if pos not in data_dict:
					data_dict[pos] = []
				if score == 'NaN':
					data_dict[pos].append(np.nan)
				else:    
					data_dict[pos].append(int(float(score)))

	df = pd.DataFrame.from_dict(data_dict, orient="index", columns=col_names)

	mask = df.isnull() # the missing regions or gaps in the alignment


	sns.set(rc = {'figure.figsize':(15,10)})
	ax = sns.heatmap(df.T,mask=mask.T,annot=False, cmap='inferno',vmin = 1, vmax = 9,center = 5,fmt='g')
	ax.invert_yaxis()
	ax.set_facecolor('xkcd:gray') # gaps are kept in grey

	plt.savefig(output,format="png",dpi=300)
	plt.clf() # to clean current figure in memory

# set Path and directories
# make sure to change the Path when running in your local directory
main_dir = Path('/Users/chakravartyd2/FixJ_KdpE/')
data_dir = main_dir / "data"
out_dir = main_dir / "plots"

output1 = out_dir / "heatmap_a.png"
output2 = out_dir / "heatmap_b.png"

# set the files needed for the heatMaps
list_files1 = ["4kfcA_ori.dat","4kfcA_ml.dat","4kfcA_con.dat"]
list_files2 = ["4kfcA_ori.dat","4kfcA_wh.dat","4kfcA_hth.dat"]

# also save the column names in a list, this will be on the Y-axis
col_names1 = ["all_MSA","ML_tree","Consensus_tree"]
col_names2 = ["all_MSA","MSA_wH","MSA_HTH"]

# call the function to save each figure
plot_heatmap(list_files1,col_names1,output1)
plot_heatmap(list_files2,col_names2,output2)


