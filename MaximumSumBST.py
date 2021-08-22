'''Maximum sum BST in binary Tree, we have to check wheter it' BST or not'''


def maximSumBST(root):
    result = 0

    def dfs(node):
        nonlocal result

        if not node:
            return 1,0,None,None

        ls,l,ll,left = dfs(node.left)
        rs,r,right,rr = dfs(node.right)

        if ((ls==2 and left<node.val) or ls == 1) and ((rs == 2 and right>node.val) or rs==1):
            size = node.val + l + r
            result = max(result,size)


            return 2,size,(ll if ll is not None else root.val),(rr if rr is not None else root.val)

        return 0,None,None,None

    dfs(root)
    return result