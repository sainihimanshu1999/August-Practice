'''In some question rather than goin one way you can go opposite and still find the answer you can get intersection of
sets using #& '''


def pacificAtlantic(grid):
    m = len(grid)
    n = len(grid[0])

    dirs = [(1,0),(-1,0),(0,1),(0,-1)]


    def dfs(i,j,visited):
        if (i,j) in visited:
            return (i,j)

        visited.add((i,j))

        for d in dirs:
            x,y = i+d[0],j+d[1]

            if 0<=x<m and 0<=y<n and grid[x][y]>=grid[i][j]:
                dfs(x,y,visited)


    pacific = set()
    atlantic = set()


    for i in range(m):
        dfs(i,0,pacific)
        dfs(i,n-1,atlantic)


    for j in range(n):
        dfs(0,j,pacific)
        dfs(m-1,j,atlantic)


    return list(pacific&atlantic)




    