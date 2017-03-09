import networkx as nx
import matplotlib.pyplot as plt

import ArcList as al

al.set_num_of_nodes(4)
al.add_edge(0,1)
al.add_edge(1,2)
al.add_edge(2,3)
al.add_edge(1,3)
al.add_edge(0,2)

al.print_lists()
graph = nx.Graph()
al.make_norm_graph(graph)
graph.nodes()

nx.draw(graph)
plt.show()