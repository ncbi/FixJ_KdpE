# load all packages required
library(treedataverse)
library(ggplot2)
library(aplot)

# set path and folders
setwd("/Users/chakravartyd2/FixJ_KdpE/")
# ancestral reconstruction was done on the Consensus tree after bootstrapping
file <- "data/asr.tree" 
tree <- read.newick(file)

# create a generic format of display for the tree
p <- ggtree(tree,size=0.5) + theme_tree2()

# To get Node labels/attributes - HTH or WH
tipcat = read.csv("data/attributes.csv", header=TRUE)
# save as data frame, each Node corresponds to a label
dd = as.data.frame(tipcat)

# Plotting the Ancestral nodes on the Consensus tree
p %<+% dd + geom_tippoint(aes(color=Name),size=2,alpha=0.5) +
  scale_color_manual(values=c("HTH"= "grey20","wH"="#f5f479"), na.translate=FALSE) +
  geom_point2(aes(subset=(label %in% c("5XSO"))), fill='grey50',color="black",
              size=6.5, alpha=1,shape=22) +
  geom_point2(aes(subset=(label %in% c("4KFC"))), fill='#f5f479',color="black",
              size=6.5, alpha=1,shape=22) +
  geom_point2(aes(subset=(label %in% c("TMD58691.1", "TMC70452.1", "TME68356.1","TMC70453.1",
                                       "TMB79520.1","OLE96773.1","TMC42982.1","TML48806.1","TML69799.1","TML69678.1","TML85299.1",
                                       "PWU22963.1"))), shape=21,size=2, fill='#bb3754', color='black',alpha=0.8) +
  geom_nodepoint(aes(subset=(label %in% c("Node2547", "Node3", "Node2","Node1",
                                          "Node 3064","Node2532","Node2539"))),
                 shape=21,size=4, fill='black') +
  theme(text = element_text(size = 18), legend.position = "none")
# save plot as png
output <- "plots/ASR_tree.png"
ggsave(output,plot=last_plot(),dpi=300,units="px", bg="transparent")

# please refer to FigS4.pptx, to see how the final figure is made
