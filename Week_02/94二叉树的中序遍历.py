# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def inorderTraversal(self, root: TreeNode) -> List[int]:
#         stack=[]
#         res=[]
#         while(root or stack):
#             while(root):
#                 stack.append(root)
#                 root=root.left
#             root=stack.pop()
#             res.append(root.val)
#             root=root.right
#         return res

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack=[('while',root)]
        res=[]
        while(stack):
            color,root=stack.pop()
            if( root is None):
                continue
            if(color=='gray'):
                res.append(root.val)
                continue
            
            stack.append(('white',root.right))
            stack.append(('gray',root))
            stack.append(('white',root.left))

        
        return res