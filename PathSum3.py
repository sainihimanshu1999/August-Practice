'''we don't have to use either root or leaf node if not necessary to give the path, in these types of questions we can use
two different functions one to simply perform the dfs and other is to count the path sum'''



def pathSum(root,targetSum):

    count = 0


    def dfs(node,target):
        if not node:
            return None

        path(node,target)
        dfs(node.left,target)
        dfs(node.right,target)


    def path(node,target):
        nonlocal count
        if not node:
            return None

        if target == node.val:
            count+=1

        path(node.left,target-node.val)
        path(node.right,target-node.val)



    dfs(root,targetSum)
    return count