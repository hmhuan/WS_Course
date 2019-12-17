import networkx as nx
import numpy as np

def graph(fileIn = None):
    """
    input: 
        fileIn: file input for graph 
    output: G
    """
    G = dict()
    G[0] = [1, 2, 3]
    G[1] = [0, 3]
    G[2] = [0]
    G[3] = [1, 2]
    return G

def pageRank(G, beta = 0.85, iter = 100, teleport_1st = None, eps = 1e-8):
    if not teleport_1st:
        teleport_1st = G.keys()
    N = len(G.keys())
    next_rank_list = [1.0/N for i in range(N)]
    curr_rank_list = next_rank_list.copy()

    for i in range(iter):
        curr_rank_list, next_rank_list = next_rank_list, curr_rank_list
        for j in range(N):
            next_rank_list[j] = 0 #(1 - beta) / N
        for node in teleport_1st:
            next_rank_list[node] = (1 - beta) / N

        for node in G:
            if G[node]:
                contribution = beta * curr_rank_list[node] / len(G[node])
                for edge in G[node]:
                    next_rank_list[edge] += contribution
        leakage_contribution = (1 - sum(next_rank_list)) / N
        for el in next_rank_list:
            el += leakage_contribution
        total_diff = 0
        for j in range(N):
            total_diff += abs(curr_rank_list[j] - next_rank_list[j])
        if total_diff < eps:
            print("iters = ", i)
            break
    return next_rank_list

G = graph()
#G[2] = [2]
rank_list = pageRank(G)
print(rank_list)
print(sum(rank_list))