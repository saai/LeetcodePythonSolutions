# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None
        min_v = min(p.val, q.val)
        max_v = max(p.val, q.val)
        if max_v > root.val and min_v < root.val:
            return root
        elif min_v > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif max_v < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif min_v == root.val or max_v == root.val:
            return root
            