class Solution:
    # @param {integer[]} inorder
    # @param {integer[]} postorder
    # @return {TreeNode}
    def buildTree(self, inorder, postorder):
        n1,n2 = len(postorder), len(inorder)
        if n1!=n2 or n1==0:
            return None
        root = TreeNode(0)
        st = []
        last_pop = root
        i= n1-1
        j = i
        while(i>=0):
            num = postorder[i]
            node = TreeNode(num)
            if last_pop:
                last_pop.left = node
                st.append(node)
                last_pop = None
            else:
                last = st[-1]
                last.right = node
                st.append(node)
            while(j >= 0 and len(st)> 0 and st[-1].val==inorder[j]):
                last_pop = st.pop()
                j -= 1
            i -= 1
        return root.left
        