# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if not root:
            return 
        st = [root]
        while(len(st)>0):
            node = st.pop()
            next_st = []
            while node:
                if node.left:
                    next_st.append(node.left)
                if node.right:
                    next_st.append(node.right)
                if len(st)>0:
                    r = st.pop()
                    node.next = r
                    node = r
                else:
                    node = None
            st += next_st[::-1]
        
                