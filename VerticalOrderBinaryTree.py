'''using defaultdict to see the order'''

from collections import defaultdict

def verticalOrder(root):
    dic = defaultdict(list)

    result = []

    left,right = float('inf'),float('-inf')

    def dfs(root,col,row):
        nonlocal left
        nonlocal right
        
        left = min(left,col)
        right = max(right,col)

        dic[col].append((row,root.val))

        if root.left: dfs(root.left,col-1,row+1)
        if root.right: dfs(root.right,col+1,row+1)

    dfs(root,0,0)

    for i in range(left,right+1):
        result += [[j for i,j in sorted(dic)]]

    return result