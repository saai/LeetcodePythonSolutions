class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
        if len(nums) == 0:
            return 0
        stack = []
        maxValue = sum = -1111111
        for i in nums:
            if i > (sum + i):
                stack = []
                stack.append(i)
                sum = i
            else:
                stack.append(i)
                sum += i
            maxValue = sum if sum>=maxValue else maxValue
                
        return maxValue
        