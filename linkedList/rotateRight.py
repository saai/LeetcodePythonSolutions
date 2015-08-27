class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 0 or not head or not head.next :
            return head
        nHead = ListNode(0)
        nHead.next = head
        end = nHead
        nEnd = nHead
        l = 0
        while(end.next != None):
            end = end.next
            l += 1
        for i in xrange(l-k%l):
            nEnd = nEnd.next
        end.next = head
        nHead.next = nEnd.next
        nEnd.next = None
        return nHead.next
        