class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        inc = 0
        exc = 0
        for num in nums:
            cur_exc = max(inc,exc)
            inc = exc + num
            exc = cur_exc
        return max(inc, exc)
            
            
        