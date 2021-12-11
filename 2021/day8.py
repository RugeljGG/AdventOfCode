# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 05:52:38 2021

@author: gape
"""

from collections import Counter, defaultdict
import aoc_helper

data = aoc_helper.get_input(8, year=2021).strip()

print('Day 8 input:')
print(data[:200])
print('Total input length: ', len(data))
print('Total input row length: ', len(data.split()))
print()


digits =     {0:'abcefg',
              1:'cf',
              2:'acdeg',
              3:'acdfg',
              4:'bcdf',
              5:'abdfg',
              6:'abdefg',
              7:'acf',
              8:'abcdefg',
              9:'abcdfg'}

mapper = {v:k for k, v in digits.items()}
total = set('abcdefg')

lens = defaultdict(list)

for w in digits.values():
    lens[len(w)].append(w)

s1 = 0
s2 = 0
for row in data.split('\n'):
    input, output = row.split('|')
    for w in output.strip().split():
        if len(w.replace('.','')) in (2,3,4,7):
            s1+=1
            
    words = input.split() + output.split()
    p1 = defaultdict(lambda: total.copy())
    p2 = defaultdict(lambda: total.copy())
    

    for word in words:
        words2 = lens[len(word)]
        w2_cands = set.union(*(set(w2) for w2 in words2))
        w2_i_cands = set.intersection(*(set(w2) for w2 in words2))
        w_cands = set(word)
        for c1 in word:
            p1[c1].intersection_update(w2_cands)
        for c2 in w2_i_cands:
            p2[c2].intersection_update(w_cands)
            
    taken1 = dict()
    taken2 = dict()
    
    while len(taken1) < 7:
        for k, v in p1.items():
            v = v-taken2.keys()
            if k in taken1:
                continue
            elif len(v) == 1:
                i = v.pop()
                taken1[k] = i
                taken2[i] = k
        for k, v in p2.items():
            v = v-taken1.keys()
            if k in taken2:
                continue
            elif len(v) == 1:
                i = v.pop()
                taken2[k] = i
                taken1[i] = k
            
    total_d = []
    for w in output.split():
        w2 = (''.join(taken1[c] for c in w))
        digit = mapper[''.join(sorted(w2))]
        total_d.append(str(digit))
    s2+=int(''.join(total_d))
        
        
        
        
        