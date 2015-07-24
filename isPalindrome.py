class Solution:
    # @param {ListNode} head
    # @return {boolean}
    def isPalindrome(self, head):
        p = head
        n = 0    
        while (p != None):
            n += 1
            p = p.next
        if n == 0 or n == 1:
            return True
        step = n/2
        p = head    
        next_p = p.next
        p.next = None
        while(step>1):
            nn = next_p.next
            next_p.next = p
            p = next_p
            next_p = nn
            step-=1
        if n%2:
            next_p = next_p.next
        while(p!=None and next_p != None):
            if p.val != next_p.val:
                return False
            p = p.next
            next_p = next_p.next
        return True
            