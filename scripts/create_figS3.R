# load all packages required
library(treedataverse)
library(ggplot2)
library(aplot)

# set path and folders
setwd("/Users/chakravartyd2/FixJ_KdpE/")
file <- "data/bootstrapped_consensus.tree"
tree <- read.newick(file, node.label='support') # read the bootstrapping values too

# display the bootstrapping colours from high (red) to low (green)
# branches in grey are also not well supported
p <- ggtree(tree,size=0.5,aes(color=support))  +
  scale_color_continuous(low='green', high='red') +
  theme(legend.position="right")

# save plot as png
output <- "plots/Consensus_bootstrappedtree.png"
ggsave(output,plot=last_plot(),dpi=300,units="px", bg="transparent")

# please refer to FigS3.pptx, to see how the final figure is made