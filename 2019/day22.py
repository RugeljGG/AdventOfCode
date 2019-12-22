# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 05:59:24 2019

@author: gape
"""

orders = list()
with open('day22.txt') as file:
    for row in file:
        if 'deal into new stack' in row:
            orders.append(('ns', None))
        elif 'cut' in row:
            n = int(row.strip()[4:])
            orders.append(('cut', n))
        elif 'deal with increment' in row:
            n = int(row.strip()[19:])
            orders.append(('deal', n))
        else:
            print('error', row)

def task1(l=10007, target=2019):
    stack = list((i for i in range(l)))
    for order, n in orders:
        if order == 'ns':
            stack = stack[::-1]
        elif order == 'cut':
            stack = stack[n:] + stack[:n]
        elif order == 'deal':
            old_stack = stack.copy()
            for i in range(len(stack)):
                stack[(i*n)%len(stack)] = old_stack[i]

    return stack.index(target)


def task2(l=119315717514047, r=101741582076661, target=2020):
    def shuffle(k):
        for order, n in orders[::-1]:
            if order == 'ns':
                k = l-1 - k
            elif order == 'cut':
                k = (k+n)%l
            elif order == 'deal':
                if k != 0:
                    move = l % n
                    for j in range(n):
                        pos = (k+j*move)
                        if pos % n == 0:
                            k = pos // n + j * (l // n)
                            break
        return k

    x = target
    y = shuffle(x)
    z = shuffle(y)

    # WOLFRAMALPHA: PowerMod[y-x,-1, l] == 103614356366691
    k = (((z - y)%l) * 103614356366691) % l
    n = (y - k*x) % l
    # WOLFRAMALPHA: {{k, n},{0, 1}}^r  = {{k^r, (k^r-1)*n/(k-1)}, {0, 1}}
    # WOLFRAMALPHA: PowerMod[k-1, -1, l] = 119081386805035
    return (pow(k, r, l)*x%l+(pow(k,r,l)-1)*n % l *119081386805035 % l)% l

print("Task 1: ", task1())
print("Task 2: ", task2())