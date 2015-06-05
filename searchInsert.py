class Solution:
	def searchInsert(self, nums, target):
        n = len(nums)
        m = n/2
        if n==0:
            return 0
        if n==1:
            if nums[0]>=target:
                return 0
            else:
                return 1
        if nums[m]==target:
            return m
        elif nums[m]>target:
            return self.searchInsert(nums[0:m],target)
        else:
            if (m+1)==n:
                return n
            else:
                return (m+1)+self.searchInsert(nums[m+1:n],target)