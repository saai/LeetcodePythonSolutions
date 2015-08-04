# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def minDepth(self, root):
        def dfs(root, depth):
            if not root:
                return depth-1
            if root.left == None and root.right == None:
                return depth
            elif root.left == None:
                return dfs(root.right, depth+1)
            elif root.right == None:
                return dfs(root.left, depth+1)
            else:
                ld = dfs(root.left, depth+1)
                rd = dfs(root.right, depth+1)
                return min(ld,rd)
        def bfs(root):
            if not root:
                return 0
            row = [root]
            d = 1
            while(row != None):
                n_row = []
                for node in row:
                    if node.left==None and node.right==None:
                        return d
                    else:
                        if node.left:
                            n_row.append(node.left)
                        if node.right:
                            n_row.append(node.right)
                row = n_row
                d += 1
            return d
        #d = dfs(root, 1)
        d = bfs(root)
        return d 