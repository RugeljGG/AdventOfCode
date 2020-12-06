# -*- coding: utf-8 -*-

import aoc_helper

data = aoc_helper.get_input(5, force=True)

print('Day 5 input (first 5 lines):')
print('\n'.join(data.split('\n')[:5]))
print('\nTotal input length: ', len(data))
print('Total input row count: ', len(data.split('\n'))-1)
print("\n############################################################\n")

best = 0
ids = set()
for row in data.split('\n')[:-1]:
    rown = int(row[:7].replace('B', '1').replace('F','0'), 2)
    coln = int(row[-3:].replace('R', '1').replace('L','0'), 2)
    
    sid = rown * 8 + coln
    if sid>best:
        best = sid
    ids.add(sid)
    
print('Part 1 answer: ', best)

last = 0
for i in range(1, best):
    if i not in ids:
        if last == i-1:
            last = i
        else:
            print('Part 2 answer: ', i)
            break