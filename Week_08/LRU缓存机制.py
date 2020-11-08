class TreeNode:
    def __init__(self,key=None,val=None):
        self.val=val
        self.key=key
        self.prev=None
        self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.hashmap={}
        self.capacity=capacity
        self.head=TreeNode()
        self.tail=TreeNode()
        self.head.next=self.tail
        self.tail.prev=self.head
    def moveTailToNode(self,key):
        node=self.hashmap[key]
        node.prev.next=node.next
        node.next.prev=node.prev
        self.tail.prev.next=node
        node.prev=self.tail.prev
        node.next=self.tail
        self.tail.prev=node

    def get(self, key: int) -> int:
        if(key in self.hashmap):
            self.moveTailToNode(key)
        ret=self.hashmap.get(key,-1)
        if(ret==-1):
            return -1
        else:
            return ret.val

    def put(self, key: int, value: int) -> None:
        if(key in self.hashmap):
            self.hashmap[key].val=value
            self.moveTailToNode(key)
        else:
            if(len(self.hashmap)==self.capacity):
                self.hashmap.pop(self.head.next.key)
                self.head.next.next.prev=self.head
                self.head.next=self.head.next.next
            newNode=TreeNode(key,value)
            self.tail.prev.next=newNode
            newNode.prev=self.tail.prev
            newNode.next=self.tail
            self.tail.prev=newNode
            self.hashmap[key]=newNode







# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)