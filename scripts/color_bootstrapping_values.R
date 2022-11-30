library("ggplot2")
library("ggtree")
library("treeio")
library(ggrepel)

setwd("/Users/chakravartyd2/fold_switching/sideproject2/data_frm_llp/")
file <- "unique_consensus.tree"
file <- "asr_data/asr.iqtree"
tr <- read.newick(file, node.label='support')

p <- ggtree(tree) + geom_nodepoint(aes(color=as.numeric(label)))
p <- ggtree(tr) + geom_nodelab(geom='label', aes(label=support, subset=support > 90))

p <- ggtree(tr, aes(color=support)) + geom_nodepoint(aes(subset=(label %in% c("Node2547", "Node3", "Node2","Node1",
                                                                              "Node 3064","Node2532","Node2539"))), 
                                                     shape=21,size=4, fill='black') +
  scale_color_continuous(low='green', high='red') +theme(legend.position="right")

# to save the plot
ggsave("plot_contree_bs.png",plot=last_plot(),dpi=2000,units="px", bg="transparent")
# try this
ggtree(tr) + 
  geom_nodepoint(aes(subset = as.numeric(label) ==100), size = 3) + 
  theme_tree()