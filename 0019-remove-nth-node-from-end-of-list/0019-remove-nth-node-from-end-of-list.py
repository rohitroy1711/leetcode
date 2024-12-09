# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0,head)
        sp = dummy
        fp = dummy
        for i in range(n+1):
            if not fp:
                return head
            fp = fp.next
        while fp:
            sp = sp.next
            fp = fp.next
        sp.next = sp.next.next
        return dummy.next