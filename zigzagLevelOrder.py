# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def zigzagLevelOrder(self, root):
        result = []
        if root == None:
            return result
        stack = []
        stack.append(root)
        result.append([root.val])
        i = 1
        while(len(stack) != 0):
            node = stack.pop()
            row = []
            while(node != None):
                if i%2: #right to left
                    if node.right != None:
                        row.append(node.right)
                    if node.left != None:
                        row.append(node.left)
                else:
                    if node.left != None:
                        row.append(node.left)
                    if node.right != None:
                        row.append(node.right)
                if len(stack) == 0:
                    break
                else:
                    node = stack.pop()
            if len(row) != 0:
                result.append([n.val for n in row])
            stack = row
            i+=1
        return result
            
