class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def canJump(self, nums):
        n = len(nums)
        if n == 0 or n == 1:
            return True
        last = n-1
        i = n-2
        while(i >= 0):
            if (i + nums[i])>=last:
                last = i
            i -= 1
        return last <= 0
    # @param {integer[]} nums
    # @return {boolean}
    def myCanJump(self, nums):
        n = len(nums)
        if n == 0 or n == 1:
            return True
        i = 0
        max_jump = nums[i]
        while(i < n):
            max_jump = max(nums[i],max_jump) 
            if max_jump == 0:
                break
            else:
                i+=1 
                max_jump -= 1 # 比上一个方法多一次赋值
        return i >= n-1    