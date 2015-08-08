# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
        prehead = ListNode(0)
        cur = prehead
        while(l1 and l2):
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
                cur = cur.next
            elif l1.val > l2.val:
                cur.next = l2
                l2 = l2.next
                cur = cur.next
            else:
                cur.next = l1
                cur = cur.next
                while(l1.next and l1.next.val == l1.val):
                    l1 = l1.next
                    cur = cur.next
                l1 = l1.next
                cur.next = l2
                cur = cur.next
                while(l2.next and l2.next.val == l2.val):
                    l2 = l2.next
                    cur = cur.next
                l2 = l2.next
        if l1:
            cur.next = l1
        elif l2:
            cur.next = l2
        return prehead.next
        
