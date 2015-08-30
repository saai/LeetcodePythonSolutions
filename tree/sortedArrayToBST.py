class Solution:
	def sortedArrayToBST(self, nums):
        n = len(nums)
        if n == 0 :
            return None
        if n == 1:
            return TreeNode(nums[0])
        m = n/2
        left_nums = nums[0:m]
        right_nums = nums[m+1:n]
        left_node = self.sortedArrayToBST(left_nums)
        right_node = self.sortedArrayToBST(right_nums)
        node = TreeNode(nums[m])
        node.left = left_node
        node.right = right_node
        return node
    