# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        nHead = ListNode(0)
        cur = head
        while(cur != None):
            nxt = cur.next
            cur.next = nHead.next
            nHead.next = cur
            cur = nxt
        return nHead.next
            