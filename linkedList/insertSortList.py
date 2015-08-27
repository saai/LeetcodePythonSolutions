# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        nHead = ListNode(0)
        p = head
        npre = nHead
        while(p!= None):
            t = p.next
            npre = nHead
            np = npre.next
            while(np!=None and p.val>np.val):
                npre = np
                np = np.next
            p.next = npre.next
            npre.next = p
            p = t
        return nHead.next