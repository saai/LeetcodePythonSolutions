# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
max_v = -2147483648
class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def maxPathSum(self, root):
        global max_v 
        max_v = -2147483648
        def dfs(root):
            if not root:
                return 0
            l = dfs(root.left)
            r = dfs (root.right)
            if l < 0:
                l = 0
            if r < 0:
                r = 0
            global max_v 
            max_v = max(max_v, root.val + l+ r)
            return root.val+ max(r,l)
        dfs(root)
        return max_v