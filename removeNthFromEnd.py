# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):
        p = head
        pre = head
        count = 1
        dist = 0
        while(p.next != None):
                p = p.next
                count += 1
                dist += 1
                while(dist > n):
                    pre = pre.next
                    dist -= 1
        if count <=n:
            return head.next
        pre.next = pre.next.next
        return head