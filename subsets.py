class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsets(self, nums):
        nums.sort()
        res = [[]]
        n = len(nums)
        for ele in nums:
            temp = []
            for ans in res:
                temp.append(ans+[ele])
            res+=temp
        return res