# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
res = 0
class Solution(object):
    def sumNumbers2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        global res
        res = 0
        path = []
        def dfs(node, path):
            if not node:
                return 
            path.append(node.val)
            global res
            if node.left == None and node.right == None:
                n = len(path)
                for i in range(n-1, -1, -1):
                    res += path[i]* (10**(n-1-i))
            dfs(node.left, path)
            dfs(node.right, path)
            path.pop()
        dfs(root,path)
        return res
        
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.traverse_sum(root, 0)
    def traverse_sum(self, node, parent_val):
        if not node:
            return 0
        if node.left == None and node.right == None:
            return parent_val*10 + node.val
        else:
            return self.traverse_sum(node.left, parent_val*10 + node.val) + \
            self.traverse_sum(node.right, parent_val*10+node.val)