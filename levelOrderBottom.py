# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def levelOrderBottom(self, root):
        res = []
        if not root:
            return res
        l = [root]
        while(l != None):
            nl = []
            row = []
            for node in l:
                row.append(node.val)
                if node.left != None:
                    nl.append(node.left)
                if node.right != None:
                    nl.append(node.right)
            res.insert(0,row)            
            if len(nl)!= 0:
                l = nl
            else:
                l = None
        return res