# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def rightSideView(self, root):
        levels = []
        res = []
        self.dfs(root, 0, levels)
        for i in xrange(len(levels)):
            res.append(levels[i][-1])
        return res
            
    def dfs(self, root, level, levels):    
        if not root:
            return 
        if level > len(levels)-1 :
            levels.append([root.val])
        else:
            levels[level].append(root.val)
        if root.left != None:
            self.dfs(root.left,level+1, levels)
        if root.right != None:
            self.dfs(root.right, level+1, levels)
            
        