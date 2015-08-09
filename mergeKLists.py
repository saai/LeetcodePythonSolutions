# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode[]} lists
    # @return {ListNode}
    def mergeKLists(self, lists):
        n = len(lists)
        if n == 0 :
            return None
        if n == 1:
            return lists[0]
        mid = n/2
        l = self.mergeKLists(lists[:mid])
        r = self.mergeKLists(lists[mid:])
        return self.mergeTwoLists(l,r)
        
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
        prehead = ListNode(0)
        cur = prehead
        while(l1 and l2):
            if l1.val < l2.val:
                cur.next = l1
                while(l1.next and l1.next.val == l1.val):
                    l1 = l1.next
                cur = l1
                l1 = l1.next
            elif l1.val > l2.val:
                cur.next = l2
                while(l2.next and l2.next.val == l2.val):
                    l2 = l2.next
                cur = l2
                l2 = l2.next
            else:
                cur.next = l1
                while(l1.next and l1.next.val == l1.val):
                    l1 = l1.next
                cur = l1
                l1 = l1.next
                cur.next = l2
                while(l2.next and l2.next.val == l2.val):
                    l2 = l2.next
                cur = l2
                l2 = l2.next
        if l1:
            cur.next = l1
        elif l2:
            cur.next = l2
        return prehead.next       
                