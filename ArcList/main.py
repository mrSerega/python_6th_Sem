import networkx as nx #this is a lib
import matplotlib.pyplot as plt #this is a lib

import ArcList as al #this is a class

myGraph = al.Arclist(4 , [0,1,2,1,0], [1,2,3,3,2])
myGraph.remove_edge(0)
myGraph.print_lists()
graph = nx.DiGraph()
myGraph.make_norm_graph(graph)
nx.draw_networkx(graph,with_labels=True)
plt.show()
