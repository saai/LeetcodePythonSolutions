# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        i = 1
        nHead = ListNode(0)
        nHead.next = head
        pre = nHead
        cur = pre.next
        while(cur!= None):
            if i < m:
                pre = pre.next
                cur = cur.next
                i += 1
                continue
            if i <=n :
                if i == m:
                    pre.next = None
                nxt = cur.next
                cur.next = pre.next
                pre.next = cur
                cur = nxt
                i += 1
                continue
            else:
                break
        while(pre.next):
            pre = pre.next
        pre.next = cur
        return nHead.next
        