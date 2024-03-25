class node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        
        
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left = node(0,0)# Lru
        self.right = node(0,0)# Mru
        
        self.left.next = self.right
        self.right.prev = self.left
    
    def insert(self,new_node):
        temp = self.right.prev
        temp.next = new_node
        new_node.prev = temp
        new_node.next = self.right
        self.right.prev = new_node
        
        
        
        
    def remove(self,node):
        prev,nxt = node.prev,node.next
        prev.next,nxt.prev = nxt,prev
        

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, val: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        elif len(self.cache) >= self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

        self.cache[key] = node(key,val)
        self.insert(self.cache[key])
  
        
             


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)