# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def preorderTraversal(self, root):
        r = []
        if root == None:
            return r
        stack = []
        new_root = TreeNode(0)
        new_root.right = root
        stack.append(new_root)
        while(len(stack)!= 0):
            node = stack.pop()
            rroot = node.right
            while(rroot!=None):
                r.append(rroot.val)
                stack.append(rroot)
                rroot = rroot.left
        return r
        