class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        n = len(nums)
        if n <=1:
            return n
        i= 0
        j = 0
        while(j < n):
            if nums[j]!=nums[i]:
                nums[i+1] = nums[j]
                i += 1    
            j +=1
        return i+1