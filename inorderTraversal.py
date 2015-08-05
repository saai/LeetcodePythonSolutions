# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def inorderTraversal(self, root):
        res = []
        st = []
        p = root
        while(p != None):
            # push
            while(p != None):
                st.append(p)
                p = p.left
            # pop
            while(len(st)>0):
                top = st.pop()
                res.append(top.val)
                if top.right :
                    p = top.right
                    break
        return res
        