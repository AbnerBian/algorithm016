# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':


# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         dic={root:None}
#         def dfs(root):
#             if(root is None):return
#             if(root.left):dic[root.left]=root
#             if(root.right):dic[root.right]=root
#             dfs(root.left)
#             dfs(root.right)

#         dfs(root)
#         l1=p
#         l2=q
#         while(l1!=l2):
#             l1=dic.get(l1,q)
#             l2=dic.get(l2,p)
#         return l1

# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         dic={root:None}
#         def dfs(root):
#             if(root is None):return
#             if(root.left):dic[root.left]=root
#             if(root.right):dic[root.right]=root
#             dfs(root.left)
#             dfs(root.right)

#         dfs(root)
#         l1=p
#         l2=q
#         while(l1!=l2):
#             l1=dic.get(l1,q)
#             l2=dic.get(l2,p)
#         return l1

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if(root is None or root==p or root==q):return root
        left=self.lowestCommonAncestor(root.left,p,q)
        right=self.lowestCommonAncestor(root.right,p,q)
        if(not right):return left
        if(not left):return right
        return root