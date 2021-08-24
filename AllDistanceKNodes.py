'''we have to use a form of dijkstra in this, where we have to use dfs to form adjancy list'''

from collections import defaultdict

def kdistance(root,target,k):
    graph = defaultdict(list)
    result = []
    visited = set()


    def dfs(node):
        if node.left:
            graph[node].append(node.left)
            graph[node.left].append(node)
            dfs(node.left)

        if node.right:
            graph[node].append(node.right)
            graph[node.right].append(node)
            dfs(node.right)


    dfs(root)

    def path(node,distance):
        if distance<k:
            visited.add(node)

            for nbr in graph[node]:
                if nbr not in visited:
                    dfs(nbr,distance+1)


        elif distance == k:
            result.append(node.val)



    path(target,0)

    return result
