class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def jump(self, nums):
        n = len(nums)
        if n == 0 or n == 1:
            return 0
        i = 0
        curmax = i+nums[i]
        nextmax = 0
        level = 0
        while(curmax<n-1):
            level += 1
            nextmax = i
            while(i<=curmax):
                nextmax = max(i+nums[i],nextmax)
                if nextmax >= n-1:
                    return level + 1
                i += 1
            curmax = nextmax
        return 1
        
            