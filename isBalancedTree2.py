# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# contains no nodes which's subtree height differs more than 1.
class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isBalanced(self, root):
        return self.dfsHeight(root) != -1
    def dfsHeight(self, root):
        if not root:
            return 0
        l = self.dfsHeight(root.left)
        if l == -1:
            return -1
        r = self.dfsHeight(root.right)
        if r == -1:
            return -1
        if abs(l-r)>1:return -1
        return 1+max(l,r)
                