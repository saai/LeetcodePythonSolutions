class Solution:
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, s, nums):
        i = 0
        j = -1
        n = len(nums)
        t = 0
        min_len = sys.maxint
        while(i<n and j <n):
            if t < s:
                j += 1
                if j >=n :
                    break
                t += nums[j]
            else:
                if min_len > (j-i+1):
                    min_len = j-i+1
                t -= nums[i]
                i += 1
        if min_len == sys.maxint:
            return 0
        else:
            return min_len