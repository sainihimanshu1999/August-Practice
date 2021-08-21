'''In this question a graph is made using a manager and subordinate relationship'''

from collections import defaultdict

def informTime(manager, headID, inform):
    result = 0
    graph = defaultdict(list)

    for i,num in manager:
        graph[num].append(i)

    def dfs(manager,time):
        nonlocal result
        result = max(result,time)

        for subord in graph[manager]:
            dfs(subord,time+inform[manager])


    dfs(headID,0)


    return result

