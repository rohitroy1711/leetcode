# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #This problem I am solving in three steps
        # Step 1 - finding out the total length of the linked list
        # Step 2 - find the middle number of the linked list
        # Step 3 - from the middle element return the remaining linked list
        
        #Variable to store the total length of the linked list
        n = 1
        tail = head
        while tail:
            n = n+1
            tail = tail.next
        
        # Calculating the middle index of the linked list
        mid = 0
        if n%2 == 0:
            mid = (n//2)
        else:
            mid = n//2+1
            
        # returning the list from mid element
        s = 1
        tail = head
        while tail:
            if s == mid:
                return tail
            else:
                s=s+1
                tail=tail.next
         