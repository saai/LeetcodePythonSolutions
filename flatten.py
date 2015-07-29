# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
prev = None 
class Solution:
    # @param {TreeNode} root
    # @return {void} Do not return anything, modify root in-place instead.
    def flatten(self, root):
        if root == None:
            return
        stack = [root]
        res = []
        p = root
        while(len(stack)!=0):
            if p == None:
                # pop
                p = stack.pop()
                res.append(p)
                if len(stack) == 0:
                    break
                top = stack[len(stack)-1]
                if top.left ==p or top.right == p:
                    p = None # continue pop
                else:
                    p = top # 
            else:
                # push
                if p.left != None:
                    stack.append(p.left)
                if p.right != None:
                    stack.append(p.right)
                if p.right != None:
                    p = p.right
                elif p.left!=None:
                    p = p.left
                else :
                    p = None
        newroot=TreeNode(0)
        q= newroot
        while(len(res)!=0):
            cur = res.pop()
            cur.left = None
            q.right = cur
            q = cur
        root = newroot.right
    def flatten2(self, root):
        if not root:
            return
        node = root
        while(node):
            if node.left:
                pre = node.left
                while(pre.right):
                    pre = pre.right
                pre.right = node.right
                node.right = node.left
                node.left = None
            node = node.right
    def flatten3(self, root):
        global prev
        prev= None
        def flattenHelper(node):
            if not node :
                return
            flattenHelper(node.right)
            flattenHelper(node.left)
            global prev
            node.right = prev
            node.left = None
            prev= node
        flattenHelper(root)
        