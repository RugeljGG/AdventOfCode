# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 05:57:23 2023

@author: gape
"""

from collections import Counter, defaultdict
from functools import cache
import re
import pandas as pd
import aoc_helper
import networkx as nx

data = aoc_helper.get_input(25, year=2023)
print('Day 25 input:')
print(data[:100])
print('Total input length: ', len(data))
print('Total input row length: ', len(data.split()))
print()

data = [d for d in data.strip().split('\n')]

G = nx.Graph()

for row in data:
    a, b = row.split(': ')
    for c in b.split(' '):
        G.add_edge(a, c)



for remove in nx.minimum_edge_cut(G):
    G.remove_edge(*remove)

g1, g2 = nx.connected_components(G)
print("Task 1 answer:", len(g1) * len(g2))
