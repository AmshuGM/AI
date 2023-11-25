#!/usr/bin/env python
# coding: utf-8

# In[8]:


def bfs(src,target):
    q=[src]
    exp=[]
    while q:
        source=q.pop(0)
        exp.append(source)
        print(source)
        if source==target:
            print('Success')
            return
        poss_moves=[]
        poss_moves=possible_moves(source,exp)
        for move in poss_moves:
            if move not in exp and move not in q:
                q.append(move)


# In[9]:


def possible_moves(state,visited):
    b=state.index(-1)
    d=[]
    if b not in [0,1,2]:
        d.append('u')
    if b not in [6,7,8]:
        d.append('d')
    if b not in [0,3,6]:
        d.append('l')
    if b not in [2,5,8]:
        d.append('r')
    avail_moves=[]
    for i in d:
        avail_moves.append(gen(state,i,b))
    return [move for move in avail_moves if move not in visited]

def gen(state,m,b):
    temp=state.copy()
    if m=='d':
        temp[b+3],temp[b]=temp[b],temp[b+3]
    if m=='u':
        temp[b-3],temp[b]=temp[b],temp[b-3]
    if m=='r':
        temp[b+1],temp[b]=temp[b],temp[b+1]
    if m=='l':
        temp[b-1],temp[b]=temp[b],temp[b-1]
    return temp


# In[ ]:


bfs([6,7,8,-1,4,5,1,2,3],[1,2,3,4,5,-1,6,7,8])

