# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 17:57:27 2023

@author: gape
"""

from collections import Counter, defaultdict
import re
import pandas as pd
import aoc_helper

data = aoc_helper.get_input(5, year=2023)
print('Day 5 input:')
print(data[:100])
print('Total input length: ', len(data))
print('Total input row length: ', len(data.split()))
print()


data_parts = [d for d in data.strip().split('\n\n')]

def part1():
    paths = []


    for part in data_parts:
        name, lines = part.strip().split(':')

        if name == 'seeds':
            for i in lines.strip().split():
                paths.append([int(i)])

        else:
            next_check = paths
            paths = []
            source, _, dest = name.split(' ')[0].split('-')
            for line in lines.strip().split('\n'):
                d_s, s_s, r = (int(i) for i in line.split())
                to_check = next_check
                next_check = []
                for path in to_check:
                    if path[-1]-s_s >= 0 and path[-1]-s_s < r:
                        path.append(path[-1]+d_s-s_s)
                        paths.append(path)
                    else:
                        next_check.append(path)

            for path in next_check:
                path.append(path[-1])
                paths.append(path)

    return min((path[-1] for path in paths))



def part2():
    paths = []


    for part in data_parts:
        name, lines = part.strip().split(':')


        if name == 'seeds':
            numbers = lines.strip().split()
            i = 0
            while i < len(numbers)-1:
                num = int(numbers[i])
                r = int(numbers[i+1])
                paths.append([(num, num+r)])
                i += 2
        else:
            next_check = paths
            paths = []
            source, _, dest = name.split(' ')[0].split('-')
            for line in lines.strip().split('\n'):
                d_s, s_s, r = (int(i) for i in line.split())
                shift = d_s - s_s
                to_check = next_check
                next_check = []
                for path in to_check:
                    previous_s, previous_e = path[-1]
                    if previous_s >= s_s and previous_e < s_s + r:
                        path.append((previous_s + shift, previous_e + shift))
                        paths.append(path)
                    elif previous_s < s_s and previous_e >= s_s and previous_e < s_s + r:
                        new1 = path[:-1] + [(previous_s, s_s-1)]
                        next_check.append(new1)

                        new2 = path[:-1] + [(s_s, previous_e)] + [(s_s + shift, previous_e+shift)]
                        paths.append(new2)

                    elif previous_s >= s_s and previous_s < s_s + r and previous_e > s_s + r:
                        new1 = path[:-1] + [(s_s+r, previous_e)]
                        next_check.append(new1)

                        new2 = path[:-1] + [(previous_s, s_s+r-1)] + [(previous_s + shift, s_s+r-1+shift)]
                        paths.append(new2)

                    elif previous_s < s_s and previous_e >= s_s + r:
                        new1 = path[:-1] + [(previous_s, s_s-1)]
                        next_check.append(new1)


                        new2 = path[:-1] + [(s_s, s_s+r-1)] + [(s_s + shift, s_s+r-1+shift)]
                        paths.append(new2)

                        new3 = path[:-1] + [(s_s+r, previous_e)]
                        next_check.append(new3)

                    else:
                        next_check.append(path)

            for path in next_check:
                path.append(path[-1])
                paths.append(path)
    return min((path[-1][0] for path in paths))


print("Task 1 answer:", part1())
print("Task 2 answer:", part2())

