# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def sortList(self, head):
        if head == None or head.next == None:
            return head
        pivot = head.val
        pre = head
        p = head.next
        sp = s = ListNode(0)
        pivot_p = head
        while(p!= None):
            if p.val == pivot:
                p.val = pivot_p.val
                pivot_p.val = pivot
                pivot_p = pivot_p.next
                pre = p
                p = p.next
            elif p.val < pivot:
                sp.next = p
                sp = sp.next
                p= p.next
                pre.next = p
            else:
                pre = p
                p = p.next
        sp.next = None
        newHead = ListNode(0)
        # smaller part
        newHead.next = self.sortList(s.next) 
        s.next = None
        np = newHead
        while(np.next != None):
            np = np.next
        # find the bigger part
        bp = head
        while(bp.next!=None and bp.next.val == pivot):
            bp = bp.next
        # sort the bigger part
        bp.next = self.sortList(bp.next)
        # link the smaller part and pivots and bigger part.
        np.next = head
        return newHead.next