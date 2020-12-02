# -*- coding: utf-8 -*-

import aoc_helper

data = aoc_helper.get_input(1)

print('Day 1 input:')
print(data)
print('Total input length: ', len(data))
print('Total input row length: ', len(data.split()))
print()

data = [int(d) for d in data.split()]

done = False
for i in data:
    for j in data:
        if i + j == 2020:
            print("Part 1 answer: ", i*j)
            done = True
            break
    if done:
        break
            
d1 = sorted(data)
done = False
for i in range(len(d1)):
    for j in range(i, len(d1)):
        if d1[i]+d1[j]>2020:
            break
        for k in range(j, len(d1)):
            if d1[i]+d1[j]+d1[k] == 2020:
                print("Part 2 answer: ", d1[i]*d1[j]*d1[k])
                done = True
                break
            elif d1[i]+d1[j]+d1[k]>2020:
                    break
    if done:
        break