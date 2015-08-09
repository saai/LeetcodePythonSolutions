# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def swapPairs(self, head):
        pre = p = head
        while(p and p.next):
            np = p.next
            p.next  = np.next
            np.next = p
            if pre == head:
                head = np
            else:
                pre.next = np
            pre = p
            p = p.next
        return head
            
            