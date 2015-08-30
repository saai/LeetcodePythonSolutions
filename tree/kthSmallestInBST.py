# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        st = []
        while(root):
            st.append(root)
            root= root.left
        
        while(k):
            node = st.pop()
            k -= 1
            if k == 0:
                return node.val
            if node.right:
                node = node.right
                while(node):
                    st.append(node)
                    node = node.left
        return -1