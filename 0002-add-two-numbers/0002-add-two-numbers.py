# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        
        def reverse(lis):
            prev = None
            current = lis
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev
        
        rl1 = reverse(l1)
        rl2 = reverse(l2)
        
        
        num1 = 0
        num2 = 0
        
        while rl1:
            num1 = num1*10+rl1.val
            rl1 = rl1.next
        while rl2:
            num2 = num2*10+rl2.val
            rl2 = rl2.next
        num = num1+num2
        
        
        dummy = ListNode(0)
        p = dummy
        if num == 0:
            return dummy
        while num:
            n = num%10
            num = num//10
            p.next = ListNode(n)
            p = p.next
        return dummy.next
            
            