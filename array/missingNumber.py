class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {-1:0}
        for num in nums:
            if num not in d:
                d[num] = num + 1
        key = 0
        while(key in d):
            key = d[key]
        return key