"""
Displays a NetworkX lollipop graph to screen using a ArcPlot.
"""

from nxviz.plots import ArcPlot
import numpy.random as npr
import networkx as nx
import matplotlib.pyplot as plt

G = nx.lollipop_graph(m=10, n=4)
for n, d in G.nodes(data=True):
    G.node[n]['value'] = npr.normal()
c = ArcPlot(G, node_color='value', node_order='value')
c.draw()
plt.show()
