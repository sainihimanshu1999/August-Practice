'''In this, we have used basic dfs function with greater use of counter, good use of counter can help in various questions'''

from collections import defaultdict
from collections import Counter

def sameLabels(labels,edges,n):

    graph = defaultdict(list)
    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)


    result = [0]*n


    def dfs(node,parent):

        counter = Counter()

        for child in graph[node]:
            if child == parent:
                continue

            counter += dfs(child,node)


        counter[labels[node]]  += 1
        result[node] = counter[labels[node]]

        return counter



    dfs(0,None)
    return result

