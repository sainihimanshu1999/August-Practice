'''In lelvel order of complete binary tree, null node will not be present in between non null node, after nulll nodes
all the nodes will be null'''


def completeBinary(root):
    flag = False

    q = [root]

    while q:
        node=  q.pop(0)

        if not node:
            flag  = True
            continue

        if flag == True:
            return False

        q.append(node.left)
        q.append(node.right)


    return True