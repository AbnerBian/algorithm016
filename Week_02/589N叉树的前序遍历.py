class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if(not root):return []
        stack=[root]
        res=[]
        while(stack):
            root=stack.pop()
            res.append(root.val)
            for child in root.children[::-1]:
                stack.append(child)
        return res
        
        
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if(not root):return []
        stack=[('white',root)]
        res=[]
        while(stack):
            color,root=stack.pop()
            if(root==None):continue
            if(color=='gray'):
                res.append(root.val)
            else:
                for child in root.children[::-1]:
                    stack.append(('white',child))
                stack.append(('gray',root))
        return res
