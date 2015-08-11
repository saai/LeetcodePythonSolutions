class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        n = len(nums)
        dict = {}
        for i in xrange(n):
            t = target - nums[i]
            if t in dict:
                return [dict[t]+1,i+1]
            dict[nums[i]] = i
        return []
                    