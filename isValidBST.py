# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isValidBST(self, root):
        p = root
        st = []
        last_pop = None
        while(p != None):
            #push
            while(p != None):
                if last_pop and p.val <= last_pop.val:
                    return False
                for q in st:
                    if p.val >= q.val:
                        return False
                st.append(p)
                p = p.left
                if p != None :
                    if p.val >= st[-1].val: # cur.left >= cur
                        return False
            #pop
            while(len(st) > 0):
                last_pop = top = st.pop()
                if top.right:
                    if (top.right.val <= top.val): # cur.right <= cur 
                        return False 
                    p = top.right
                    break
        return True
        
    def isValidBST1(self, root):
        if not root:
            return True
        inorder = []
        st = []
        p = root
        while(p != None):
            while(p != None):
                st.append(p)
                p = p.left
            while(len(st) > 0):
                top = st.pop()
                inorder.append(top.val)
                if top.right :
                    p = top.right
                    break
        n = len(inorder)
        if n <= 1:
            return True
        for i in range(1,n):
            if inorder[i-1] >= inorder[i]:
                return False
        return True