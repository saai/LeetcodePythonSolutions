class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
        n = len(nums)
        i = -1
        j = 0
        while(j < n):
            if nums[j]!=val:
                nums[i+1] = nums[j]
                i += 1
            j += 1
        return i+1
            