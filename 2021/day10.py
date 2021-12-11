# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 07:43:22 2021

@author: gape
"""

from collections import Counter, defaultdict
import aoc_helper

data = aoc_helper.get_input(10, year=2021).strip()

print('Day 10 input:')
print(data[:200])
print('Total input length: ', len(data))
print('Total input row length: ', len(data.split()))
print()


s = 0

mapper = {'(':')',
          '[':']',
          '{':'}',
          '<':'>',
          }

costs = {')':3,
         ']':57,
         '}':1197,
         '>':25137,
         }

costs2 = {')':1,
         ']':2,
         '}':3,
         '>':4,
         }
      
        
s = 0
totals = []
for row in data.strip().split('\n'):
    current = list()
    ts = 0
    for c in row:
        if c in mapper.keys():
            current.append(c)
        elif c == mapper[current[-1]]:
            current.pop()
        else:
            s += costs[c]
            break
    else:
        for c in current[::-1]:
            ts *= 5
            ts += costs2[mapper[c]]
        totals.append(ts)
    
print("Part 1 answer:", s)
print("Part 2 answer:", sorted(totals)[len(totals)//2])