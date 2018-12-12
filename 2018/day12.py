# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 05:56:59 2018

@author: Gape
"""



def task1():
    steps = []
    with open('day12.txt') as file:
        state = list(next(file).strip().split(': ')[1])
        next(file)
        for row in file:
            row = row.strip().split(' => ')
            steps.append(row)
            
    generations = 20
    #generations = 50000000000
    append = ['.' for i in range(generations)] 
    prepend = ['.' for i in range(generations)] 
    
    state = prepend + state + append
    
    for g in range(generations):
        print(''.join(state))
        new_state=state.copy()
        for i in range(len(state)):
            if i < 2:
                cur = state[i-2:]
                cur += state[:5-len(cur)]
            else:
                cur = state[i-2:i+2+1]
            cur = ''.join(cur)
            
            for pattern, step in steps:
                if cur == pattern:
                    new_state[i] = step
                    break
            else:
                new_state[i] = '.'
        state = new_state
        
        
    print(sum(i-generations if s=='#' else 0 for i, s in enumerate(state)))
              
def task2():
    steps = []
    with open('day12.txt') as file:
        state = list(next(file).strip().split(': ')[1])
        next(file)
        for row in file:
            row = row.strip().split(' => ')
            steps.append(row)
            
    generations = 1000
    max_generations = 50000000000
    append = ['.' for i in range(generations)] 
    prepend = ['.' for i in range(generations)] 
    
    state = prepend + state + append
    
    past_states = dict()
    for g in range(generations):
    #    print(''.join(state))
        if g%10 == 0:
            print(g)
        new_state=state.copy()
        for i in range(len(state)):
            if i < 2:
                cur = state[i-2:]
                cur += state[:5-len(cur)]
            else:
                cur = state[i-2:i+2+1]
            cur = ''.join(cur)
            
            for pattern, step in steps:
                if cur == pattern:
                    new_state[i] = step
                    break
            else:
                new_state[i] = '.'
        
        first = new_state.index('#')
        last = new_state[::-1].index('#')
        ss = ''.join(new_state[first:-last])
        if ss in past_states.keys():
            repeat_n = g - past_states[ss][0] # po koliko rundah se ponovi
            # na srečo je n == 1,  drugače bi bila koda bolj zapletena
            repeat_i = first - past_states[ss][1] # za koliko se premakne
            current = sum(i-generations if s=='#' else 0 for i, s in enumerate(state))
            return current + (max_generations - g) * ss.count('#') * repeat_i
        state = new_state
    #    past_states[ss]=(sum(i if s=='#' else 0 for i, s in enumerate(ss)))
        past_states[ss]=(g, first, last)