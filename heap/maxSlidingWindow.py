class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        tmp = [] # tmp[0] always save the current windows max
        for i in xrange(len(nums)):
            if i < k-1: # first k-1 numbers 
                while tmp and nums[tmp[-1]]<nums[i]: # keep tmp[0] the max
                    tmp.pop()
                tmp.append(i)
                continue
            while tmp and nums[tmp[-1]] < nums[i]: # find proper location for nums[i]
                tmp.pop()
            tmp.append(i)
            while tmp and tmp[0]<= i-k: #pop the old max values
                tmp.pop(0)
            res.append(nums[tmp[0]])
        return res 
            
                
            
                
        