# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def countNodes(self, root):
        if not root:
            return 0
        h1=h2=0
        node=root
        while node:
            h1+=1
            node=node.left
        node=root
        while node:
            h2+=1
            node=node.right
        if h1==h2:
            return 2**h1-1
        return self.countNodes(root.left)+self.countNodes(root.right)+1
 