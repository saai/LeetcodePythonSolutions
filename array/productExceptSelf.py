class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        n = len(nums)
        res = [0 for i in xrange(n)]
        res[0] = 1
        for i in range(1,n):
            res[i] = res[i-1] * nums[i-1] # res[i] stands for the product of nums before i
        right_prod = 1
        for i in range(n-1,-1,-1):
            res[i] *= right_prod
            right_prod *= nums[i]
        return res