class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return 0
        minV = min(nums)
        maxV = max(nums)
        bucket_size = max(1, (maxV-minV)/(n-1))
        bucket_num = (maxV-minV)/bucket_size + 1
        if bucket_num <= 1:
            return maxV-minV
        bucket_count = [0]*bucket_num
        bucket_min = [sys.maxint]*bucket_num
        bucket_max = [-sys.maxint-1]*bucket_num
        for i in xrange(n):
            idx = (nums[i] - minV)/bucket_size
            bucket_count[idx] += 1
            bucket_min[idx] = min(bucket_min[idx], nums[i])
            bucket_max[idx] = max(bucket_max[idx],nums[i])
        last_max = minV
        maxGap = 0
        for i in xrange(bucket_num):
            if bucket_count[i] > 0:
                maxGap = max(bucket_min[i] - last_max, maxGap)
                last_max = bucket_max[i]
        return maxGap