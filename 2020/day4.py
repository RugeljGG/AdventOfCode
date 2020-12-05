# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 05:53:32 2020

@author: gape
"""

import aoc_helper
import re

data = aoc_helper.get_input(4, force=True)

print('Day 4 input:')
print(data)
print('Total input length: ', len(data))
print('Total input row length: ', len(data.split('\n'))-1)
print("\n############################################################\n")

fields = ['byr', 'iyr','eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']

passports = []
for row in data.split('\n\n'):
    passport = dict()
    for p in row.split():
        k, v = p.split(':')
        passport[k] = v
    passports.append(passport)
    

count = 0
for p in passports:
    for f in fields:
        if f =='cid':
            continue
        elif f not in p:
            break  
    else:
        # print(len(p), p)
        count+=1
        
print('Part 1 answer:', count)

count = 0
for p in passports:
    for f in fields:
        if f =='cid':
            continue
        elif f not in p:
            break
        else:
            if f == 'byr':
                v = int(p[f])
                if v <1920 or v>2002:
                    break
            if f == 'iyr':
                v = int(p[f])
                if v <2010 or v>2020:
                    break
            if f == 'eyr':
                v = int(p[f])
                if v <2020 or v>2030:
                    break
            if f == 'hgt':
                v = p[f]
                if v[-2:] == 'cm':
                    v = int(v[:-2])
                    if v <150 or v>193:
                        break
                elif v[-2:] == 'in':
                    v = int(v[:-2])
                    if v <59 or v>76:
                        break
                else:
                    break
            if f == 'hcl':
                v = p[f]
                if re.match('^#[\da-f]{6}$', v) is None:
                    break
            if f == 'ecl':
                v = p[f]
                if v not in ('amb', 'blu', 'brn', 'gry', 'grn' ,'hzl' ,'oth'):
                    break
            if f == 'pid':
                v = p[f]
                if re.match('^\d{9}$', v) is None:
                    break
                        
                
    else:
        # print(len(p), p)
        count+=1
        
print('Part 2 answer:', count)