class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_t = {}
        max_len = 0
        for num in nums:
            if num in len_t:
                continue
            else:
                left = len_t[num-1] if (num-1) in len_t else 0
                right = len_t[num+1] if (num+1) in len_t else 0
                sum = left+right+1
                if max_len < sum:
                    max_len = sum
                len_t[num] = sum
                len_t[num-left] = sum #left bounds
                len_t[num+right] = sum #right bounds
        return max_len