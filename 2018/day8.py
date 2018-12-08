# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 09:10:17 2018

@author: Gape
"""

with open('day8.txt') as file:
    data = [int(c) for c in next(file).split(' ')]
    

def task1(data):  
    def process(data):
        i = 0
        childs = data[i]
        num_meta = data[i+1]
        metadata = 0
        i+=2
    #    print(childs, num_meta)
        for j in range(childs):
            l, m = process(data[i:])
            i += l
            metadata += m
        
        metadata += sum(data[i:i+num_meta])
        return i+num_meta, metadata
    
    i = 0
    metadata = 0
    while i < len(data):
        l, m = process(data[i:])
        i += l
        metadata += m
        
    return metadata


def task2(data):
    def process(data):
        i = 0
        childs = data[i]
        num_meta = data[i+1]
        metadata = 0
        i+=2
    #    print(childs, num_meta)
        metas = []
        for j in range(childs):
            l, m = process(data[i:])
            i += l
            metas.append(m)
        
        if childs > 0:
            for j in data[i:i+num_meta]:
    #            print(j, metas)
                if j == 0:
                    continue
                try:
                    metadata += metas[j-1]
                except IndexError:
                    pass
                
        else:
            metadata += sum(data[i:i+num_meta])
        return i+num_meta, metadata
    
    i = 0
    metadata = 0
    while i < len(data):
        l, m = process(data[i:])
        i += l
        metadata += m
        
    return metadata
    
