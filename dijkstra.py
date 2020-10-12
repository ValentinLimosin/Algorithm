# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 11:28:06 2019

@author: Thebiggoliath
"""

Inf=1000
G = [[Inf,7,1,Inf,Inf,Inf],[Inf,Inf,Inf,4,Inf,1],[Inf,5,Inf,Inf,2,7],[Inf,Inf,Inf,Inf,Inf,Inf],[Inf,2,Inf,5,Inf,Inf],[Inf,Inf,Inf,Inf,3,Inf]]

def dijsktra(G):
    n = len(G)
    l,p = [Inf for _ in range(n)],[-1 for _ in range(n)]
    l[0] = 0
    p[0] = 0
    for x in range(1,n):
        if G[0][x] < Inf:
            l[x] = G[0][x]
            p[x] = 0
            
    M,V = {0},set(range(0,n))
    
    while(M != V):
        x = l.index(min(l[x] for x in (V-M)))
        for y in (V-M):
            if l[y] > l[x] + G[x][y]:
                l[y] = l[x] + G[x][y]
                p[y] = x
        M.add(x)
    print(l,p)

dijsktra(G)