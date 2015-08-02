# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {integer[]} preorder
    # @param {integer[]} inorder
    # @return {TreeNode}
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        n1,n2 = len(preorder), len(inorder)
        if n1!=n2 or n1 == 0:
            return None
        root = TreeNode(0)
        st = [root]
        i = 0
        j = 0
        last_pop= root
        while(i < n1):
            num = preorder[i]
            node = TreeNode(num)
            if last_pop != None:
                last_pop.right = node
                st.append(node)
                last_pop = None
            else:
                last = st[-1]
                last.left = node
                st.append(node)
            while(j < n1 and st[-1].val == inorder[j]):
                last_pop = st.pop()
                j += 1
            i+=1
        return root.right
                