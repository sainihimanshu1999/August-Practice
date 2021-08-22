'''In this question we have to mirror or just invert a bst, we are doing it by basic recurrsion and swapping tree.right,
tree.left branches'''



def mirror(root):
    if root:
        root.left,root.right = root.right,root.left
        mirror(root.left)
        mirror(root.right)
        return root


