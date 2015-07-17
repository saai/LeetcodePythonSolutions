# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if head == None:
            return None
        p = head
        #1st link the copy node in old list , put copy node right back relative node.
        while(p!=None):
            next  = p.next
            copy = RandomListNode(p.label)
            p.next = copy
            copy.next = next
            p= p.next.next
        #2nd link copy node random to relative copy node according to old nodes relation
        p = head
        while(p != None):
            if p.random != None:
                copy = p.next
                copy.random = p.random.next
            p = p.next.next
        #3rd break the connection of copy list and old list
        precopyhead = RandomListNode(0)
        cp = precopyhead
        p = head
        while(p != None):
            cp.next = p.next
            cp = cp.next
            
            p.next = p.next.next
            p = p.next
            
        return precopyhead.next
            