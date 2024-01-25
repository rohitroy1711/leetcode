class ListNode:
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.next = None
class MyLinkedList:

    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left
        

    def get(self, index: int) -> int:
        cur = self.left.next
        i = 0
        while cur and i<index:
            cur = cur.next
            i = i+1
        if i== index and cur and cur!=self.right:
            return cur.val  
        return -1

    def addAtHead(self, val: int) -> None:
        node,next,prev = ListNode(val),self.left.next,self.left
        next.prev = node
        prev.next = node
        node.prev = prev
        node.next = next
        

    def addAtTail(self, val: int) -> None:
        node,next,prev = ListNode(val),self.right,self.right.prev
        next.prev = node
        prev.next = node
        node.prev = prev
        node.next = next
        

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.left.next
        while cur and index>0:
            cur = cur.next
            index -=1
        if cur and index == 0:
            node,next,prev = ListNode(val),cur,cur.prev
            next.prev = node
            prev.next = node
            node.prev = prev
            node.next = next
            
        

    def deleteAtIndex(self, index: int) -> None:
        cur = self.left.next
        while cur and index>0:
            cur = cur.next
            index -=1
        if cur and index == 0 and cur!=self.right:
            next,prev = cur.next,cur.prev
            next.prev = prev
            prev.next = next
            
            
            
            


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)