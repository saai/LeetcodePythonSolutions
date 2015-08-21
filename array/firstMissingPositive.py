class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pint_t = {0:1}
        for num in nums:
            if num > 0 and num not in pint_t :
                pint_t[num] = num + 1
        key = 0
        while(key in pint_t):
            key = pint_t[key]
        return key