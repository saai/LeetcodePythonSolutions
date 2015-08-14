class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        res = []
        i = 0
        while(i < len(nums)):
            j = i
            while(j+1 < len(nums) and nums[j+1]-nums[j]<= 1):
                j += 1
            if j != i:
                res.append(str(nums[i])+'->'+str(nums[j]))
            else:
                res.append(str(nums[j]))
            i = j + 1
        return res