'''This problem is solved using basic djikstra's algorithm'''

from collections import defaultdict


def cheapestFlight(flights,src,dst,k):

    graph = defaultdict(list)
    visited = defaultdict(lambda:float('inf'))


    for u,v,c in flights:
        graph[u].append((v,c))



    q = [(src,-1,0)]


    while q:
        node,x,cost = q.pop(0)

        if node == dst or x == k:
            continue


        for nbr,c in graph[node]:
            if cost+c>=visited[nbr]:
                continue
            else:
                visited[nbr] = cost+c
                q.append((nbr,x+1,cost+c))


    return visited[dst] if visited[dst]<float('inf') else -1