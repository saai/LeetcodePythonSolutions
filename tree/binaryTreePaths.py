# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        path = []
        res = []
        self.traverse(root, path, res)
        return res
    def traverse(self, node, path, res):
        if not node:
            return
        path.append(node.val)
        if node.left == None and node.right == None:
            res.append('->'.join([str(p) for p in path[:]]))
        if node.left:
            self.traverse(node.left, path, res)
        if node.right:
            self.traverse(node.right, path, res)
        path.pop()