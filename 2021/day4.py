# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 09:17:49 2021

@author: gape
"""

from collections import Counter
import aoc_helper

data = aoc_helper.get_input(4, year=2021).strip()

print('Day 4 input:')
print(data[:200])
print('Total input length: ', len(data))
print('Total input row length: ', len(data.split()))
print()

data = data.split('\n')
nums = [int(i) for i in data[0].split(',')]



boards = []

board = dict()
j=0
for row in data[2:]:
    if row == '':
        boards.append({'data':board})
        boards[-1]['rows'] = Counter()
        boards[-1]['cols']= Counter()
        board = dict()
        j = 0
    else:
        for i, n in enumerate(row.split()):
            n = int(n.strip())
            board[n] = [i, j]
        j += 1

best = None
winners = []
for winner in nums:
    for board in boards:
        if board.get('win'):
            continue
        if winner in board['data']:
            row, col =  board['data'].pop(winner)
            board['rows'][row] += 1
            board['cols'][col] += 1
            if board['rows'][row] >= 5 or board['cols'][col] >= 5:
                winners.append(board)
                board['win'] = winner
                
                
print('Part 1 answer:', sum(winners[0]['data'].keys())*winners[0]['win'] )
print('Part 2 answer:', sum(winners[-1]['data'].keys())*winners[-1]['win'] )