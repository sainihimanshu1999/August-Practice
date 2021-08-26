'''For checkcing any kind of partition in the graph, coloring is the one way to check so in we color the opposite set as
different color than us and we use BFS in this problem'''



def bipartite(graph):
    n = len(graph)
    visited = {}


    for i in range(len(graph)):
        if i not in visited:
            if not bfs(graph,i,visited):
                return False

    return True


def bfs(graph,start,visited):
    q = [(start,1)]

    while q:
        node,color = q.pop(0)

        if node in visited:
            if visited[node] != color:
                return False


            continue

        visited[node] = color

        for v in graph[node]:
            q.append((v,-color))


    return False

