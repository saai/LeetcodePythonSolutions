# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} sum
    # @return {integer[][]}
    
    def pathSum(self, root, sum):
        res = []
        st = []
        p = root
        last_pop = None
        while(p != None):
            while(p != None):
                st.append(p)
                p = p.left
            t = st[-1]
            if not t.left and not t.right:
                v = 0
                for q in st:
                    v += q.val
                if v == sum:
                    res.append([q.val for q in st])
            while(len(st) > 0):
                top = st[-1]
                if top.right and top.right != last_pop:
                    p = top.right
                    break
                else:
                    last_pop = st.pop()
        return res      