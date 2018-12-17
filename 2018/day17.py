# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 06:01:01 2018

@author: Gape
"""

import re

xmin = None
xmax = None
ymin = None
ymax = None
clays = []
with open('day17.txt') as file:
    for row in file:
        parsed = re.findall('(.)=(\d*), .=(\d*)\.\.(\d*)', row)
        p = parsed[0]
        if p[0] == 'y':
            y = ys = int(p[1])
            xs = int(p[2])
            for i in range(int(p[3])-xs+1):
                x = xs+i
                clays.append((x, y))
        else:
            ys = int(p[2])
            x = xs = int(p[1])
            for i in range(int(p[3])-ys+1):
                y = ys+i
                clays.append((x, y))
        
        if ymin is None or ys<ymin:
            ymin = ys
        if ymax is None or y>ymax:
            ymax = y

        if xmin is None or xs<xmin:
            xmin = xs
        if xmax is None or x>xmax:
            xmax = x
        

zone = [['.' for x in range(xmax-xmin+1+10)] for y in range(ymax+1)]

for x, y in clays:
    zone[y][x-xmin+5] = '#'

y = ymin-1
x = 500-xmin+5

zone[y][x] = '+'

def print_zone():
    for i, row in enumerate(zone):
        print(i, ''.join(row))
        
        
def flow(x, y, existing):
    ys = y
    passed = 0
    while y<ymax and y >= ys:
#        print_zone()
#        print()
        if zone[y+1][x] == '.':
            y+=1
            zone[y][x] = '|'
            existing.add((x,y))
        elif zone[y+1][x] == '|':
            # spodi je že voda
            return -1, existing
        else:
            xs = x
            passable = []
            last_line = []
            liquid = False
            while zone[y][x+1] == '.':
                x += 1
                zone[y][x] = '|'
                last_line.append((x, y))
                existing.add((x,y))
                if zone[y+1][x] == '.':
                    passable.append(x)
                    break
            if zone[y][x+1] == '|' and (x+1,y) not in existing:
                liquid = True
            x = xs
            while zone[y][x-1] == '.':
                x -= 1
                zone[y][x] = '|'
                last_line.append((x, y))
                existing.add((x,y))
                if zone[y+1][x] == '.':
                    passable.append(x)
                    break
                
            if zone[y][x-1] == '|' and (x-1,y) not in existing:
                liquid = True
                
            passed = 0
            
            for p in passable:
#                print(p, y)
#                for row in zone[max((y-15,0)):y+15]:
#                    print(''.join(row[max((p-25,0)):p+45]), flush=True)
#                s = input()
#                if s == 'b':
#                    return 0, existing
#                elif s == 'a':
#                    print_zone()
                pa, e = flow(p, y, existing.copy())
#                existing.update(e)
                if pa == -1:
                    liquid = True
                elif pa == 1:
                    passed = 1
            if passed>0:
                break
            else:
                x = xs
                if not liquid:
                    zone[y][x] = '~'
                    for xl, yl in last_line:
                        zone[yl][xl] = '~'
                
                y-=1

#    print((x,y, ys))
#    raise Exception    
    if y==ymax or passed > 0:
        return 1, existing
    else:
        return 0, existing
    
flow(x, y, set())
#print_zone()

print(sum(row.count('|') for row in zone[ymin:]) + sum(row.count('~') for row in zone[ymin:]))
print((sum(row.count('~') for row in zone[ymin:])))