# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# no leaf node differs more than 1, if there is only one node, the height should be less than 2.
count = 0
min_b_d = -1
max_b_d = 1

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isBalanced(self, root):
        if not root:
            return True
        global count, min_b_d, max_leaf_d
        count = 0
        min_b_d = -1
        max_leaf_d = 1
        def dfs(root, d):
            global count, min_b_d, max_leaf_d
            if root.left == None or root.right == None:
                if min_b_d == -1:
                    min_b_d = d
                min_b_d = min(min_b_d, d)
            if root.left == None and root.right == None:
                # leaf
                count += 1
                max_leaf_d = max(max_leaf_d, d)
            else:
                if root.left != None:
                    dfs(root.left, d+1)
                if root.right != None:
                    dfs(root.right, d+1)
        dfs(root,1)
        return (max_leaf_d - min_b_d)<=1    
                