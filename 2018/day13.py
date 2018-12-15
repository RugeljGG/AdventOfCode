# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 20:47:08 2018

@author: Gašper Rugelj
"""


dirs = {'<': 2,
         '>': 0,
         '^': 1,
         'v': 3,
        }

moves = {2: (-1, 0),
         0: (1, 0),
         1: (0, -1),
         3: (0, 1),
        }


moves_n = {'/': {3:2, 2:3, 1:0, 0:1},
           '\\': {3:0, 0:3, 1:2, 2:1}
        }

class Cart():
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = dirs[direction]
        self.rotates = 0
        self.crashed = False

    def __lt__(self, other):
        if self.y < other.y:
            return True
        elif self.y == other.y and self.x < other.x:
            return True
        else:
            return False

    def move(self, tracks):
        m = moves[self.direction]
        self.x += m[0]
        self.y += m[1]
        next_t = tracks[self.y][self.x]
        if next_t in moves_n.keys():
            self.direction = moves_n[next_t][self.direction]
        elif next_t == '+':
            self.direction = (self.direction + 1 - self.rotates % 3) % 4
            self.rotates += 1

    def __repr__(self):
        return 'Cart ({},{}:{}|{})'.format(self.x, self.y, self.direction, self.crashed)



def task1():
    tracks = []
    carts = []
    taken = dict()
    with open('day13.txt') as file:
        for y, row in enumerate(file):
            track = []
            for x, c in enumerate(row):
    #            print(c)
                if c in ('<', '>') :
                    track.append('-')
                elif c in ('v', '^'):
                    track.append('|')
                else:
                    track.append(c)
                    continue
                cart = Cart(x, y, c)
                carts.append(cart)
                taken[(cart.x, cart.y)] = cart
            tracks.append(track)
    
    crash = False
    while not crash:
        carts.sort()
    #    print(carts)
        for cart in carts:
            taken.pop((cart.x, cart.y))
            cart.move(tracks)
            coords = (cart.x, cart.y)
            if coords in taken:
                crash = True
                break
            else:
                taken[coords]=cart
    return coords


def task2():
    tracks = []
    carts = []
    taken = dict()
    with open('day13.txt') as file:
        for y, row in enumerate(file):
            track = []
            for x, c in enumerate(row):
    #            print(c)
                if c in ('<', '>') :
                    track.append('-')
                elif c in ('v', '^'):
                    track.append('|')
                else:
                    track.append(c)
                    continue
                cart = Cart(x, y, c)
                carts.append(cart)
                taken[(cart.x, cart.y)] = cart
            tracks.append(track)
    
    while len(carts)>1:
        carts.sort()
    #    print(carts)
        for cart in carts:
            if cart.crashed:
                continue
            taken.pop((cart.x, cart.y))
            cart.move(tracks)
            coords = (cart.x, cart.y)
            if coords in taken:
                cart.crashed = True
                other = taken.pop((cart.x, cart.y))
                other.crashed = True
            else:
                taken[coords]=cart
            
    #    print(len(carts))
        carts = [cart for cart in carts if not cart.crashed]
    return carts[0].x, carts[0].y