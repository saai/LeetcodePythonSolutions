class Solution:
	def sortedListToBST(self,head, n):
        if head==None:
            return None
        if n == 0:
            return None
        if n == 1:
            return TreeNode(head.val)
        m = n/2
        i = 0
        p = head
        while i<m:
            p = p.next
            i+=1
        node = TreeNode(p.val)
        node.left = self.sLToBST(head,m)
        node.right = self.sLToBST(p.next,n-m-1)
        return node
