class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(self.robHelper(nums,0,len(nums)-2),self.robHelper(nums, 1,len(nums)-1))
        
    def robHelper(self, nums, start, end):
        inc = 0
        exc = 0
        for i in range(start, end+1):
            num = nums[i]
            cur_exc = max(inc, exc)
            inc = exc+num
            exc = cur_exc
        return max(inc, exc)
        