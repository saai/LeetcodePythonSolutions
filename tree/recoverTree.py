# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {void} Do not return anything, modify root in-place instead.
    def recoverTree(self, root):
        st = []
        p = root
        last = a = b =None
        while(p!=None):
            while(p!=None):
                st.append(p)
                p = p.left
            while(len(st)>0):
                top  = st.pop()
                if last and last.val >= top.val:
                    if not a:
                        a = last # the node is neighbor
                        b = top
                    else:
                        b = top # the node is seperated
                last = top
                if top.right:
                    p = top.right
                    break
        if not a or not b:
            return 
        temp = a.val
        a.val = b.val
        b.val = temp