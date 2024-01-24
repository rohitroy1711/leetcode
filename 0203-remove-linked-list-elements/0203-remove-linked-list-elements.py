# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # There are three cases in this problem
        # case 1 - head being as the removing value
        # case 2 - the value that need to be removed is somewhere inn between the linked list
        # case 3 - all the elements in the linked list are same as the value that needs to be removed.
        dummy = ListNode(-1)
        dummy.next = head
        curr = head
        pre = dummy
        
        while curr:
            if curr.val == val:
                pre.next=curr.next
            else:
                pre = pre.next
            curr = curr.next
        return dummy.next
                