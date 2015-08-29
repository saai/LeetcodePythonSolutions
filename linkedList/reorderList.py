# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        slow = head
        fast = head
        while(slow and fast.next and fast.next.next):
            slow = slow.next
            fast = fast.next.next
        p1 = head
        p2 = self.reverseList(slow.next)
        slow.next = None
        while(p1 and p2):
            nxt1 = p1.next
            nxt2 = p2.next
            p1.next = p2
            if nxt1:
                p2.next = nxt1
            p1 = nxt1
            p2 = nxt2
            
    def reverseList(self, head):
        nHead = ListNode(0)
        cur = head
        while(cur!= None):
            nxt = cur.next
            cur.next = nHead.next
            nHead.next = cur
            cur = nxt
        return nHead.next