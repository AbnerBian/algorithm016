"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if(not root):
            return []
        res=[]
        stack=[root]
        while(stack):
            res.append([node.val for node in stack])
            stack=[node for root in stack for node in root.children]
        
        return res