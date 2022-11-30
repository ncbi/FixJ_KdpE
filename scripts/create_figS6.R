# load all packages required
library(treedataverse)
library(ggplot2)
library(aplot)

# set path and folders
setwd("/Users/chakravartyd2/FixJ_KdpE/")

# To get Node labels/attributes - HTH or WH
tipcat = read.csv("data/attributes.csv", header=TRUE)
# save as data frame, each Node corresponds to a label
dd = as.data.frame(tipcat)

# all trees in the list, please refer to data/trees_of_interest.csv for more info
# on the trees
tree_list <- list(1, 6, 7, 8, 7, 24, 25, 26, 29, 30, 31, 49, 109, 111, 112, 116, 
                  1128, 1161, 2613)
# go through all the trees in the list
# find the Node for the bridge sequences
# create individual tree plots and save them
for (t in tree_list) {
  file <- paste0("data/Tree",t,".tree",sep="")
  tree <-read.nexus(file)
  p <- ggtree(tree,size=0.5) + theme_tree2()
  bridge <- getMRCA(tree, c("TME68356.1","PWU22963.1"))
  p %<+% dd + geom_tippoint(aes(color=Name),size=2,alpha=0.4) +
    scale_color_manual(values=c("HTH"= "grey20","wH"="#f5f479"), na.translate=FALSE) +
    geom_point2(aes(subset=node==bridge), fill='#bb3754',color="black",size=10, alpha=1,shape=22) +
    theme(text = element_text(size = 16)) + theme(legend.position = "none")   
  
  output <- paste0("plots/FigS6/plot_tree",t,".png",sep="")
  ggsave(output,plot=last_plot(),dpi=300,units="px", bg="transparent")
}
