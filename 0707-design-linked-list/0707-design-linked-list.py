class Listnode:
    def __init__(self,val):
        self.val = val
        self.prev=None
        self.next = None
        
class MyLinkedList:

    def __init__(self):
        self.left = Listnode(0)
        self.right = Listnode(0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index: int) -> int:
        curr = self.left.next
        while curr and index>0:
            curr = curr.next
            index-=1
        if curr and curr!= self.right and index==0:
            return curr.val
        else:
            return -1
        

    def addAtHead(self, val: int) -> None:
        temp = self.left.next
        curr = Listnode(val)
        self.left.next = curr
        curr.prev = self.left
        curr.next = temp
        temp.prev = curr
        

    def addAtTail(self, val: int) -> None:
        temp = self.right.prev
        curr = Listnode(val)
        self.right.prev = curr
        curr.next = self.right
        temp.next = curr
        curr.prev = temp
        

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.left.next
        while curr and index>0:
            curr = curr.next
            index-=1
        if curr and index==0:
            node = Listnode(val)
            temp = curr.prev
            temp.next = node
            node.prev = temp
            node.next = curr
            curr.prev = node
        

    def deleteAtIndex(self, index: int) -> None:
        curr = self.left.next
        while curr and index>0:
            curr=curr.next
            index-=1
        if index ==0  and curr and curr!=self.right:
            next,prev = curr.next,curr.prev
            next.prev = prev
            prev.next = next
            


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)