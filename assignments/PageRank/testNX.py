import networkx as nx

G = nx.DiGraph()

G.add_edge(1, 6)
G.add_edge(2, 6)
G.add_edge(3, 6)
G.add_edge(4, 6)
G.add_edge(5, 6)
G.add_edge(4, 5)
G.add_edge(6, 7)

pr = nx.hits(G)
print(pr)
