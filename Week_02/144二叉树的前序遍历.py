# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack=[('white',root)]
        res=[]
        while(stack):
            color,root=stack.pop()
            if(not root):
                continue
            if(color=='white'):
                stack.append(('white',root.right))
                stack.append(('white',root.left))
                stack.append(('gray',root))
            else:
                res.append(root.val)
        return res