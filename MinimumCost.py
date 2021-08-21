'''
In this types of questions we have to use defaultdict for our graph and then we have to use Dikstra's theoram
'''

from heapq import *
from collections import defaultdict

def minCost(maxTime,edges,passingFees):

    graph = defaultdict(list)

    for u,v,t in edges:
        graph[u].append((v,t))
        graph[v].append((u,t))


    visited = {}

    heap = [(passingFees[0],0,0)]

    while heap:
        cost,time,node = heappop(heap)

        if time>maxTime:
            continue

        if node == len(passingFees)-1:
            return cost

        if node not in visited or visited[node]>time:
            visited[node] = time

            for nbr,trip in graph[node]:
                heappush(heap,(passingFees[nbr]+cost,trip+time,nbr))


    return -1



maxTime = 30
edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]]
passingFees = [5,1,2,20,20,3]


print(minCost(maxTime,edges,passingFees))