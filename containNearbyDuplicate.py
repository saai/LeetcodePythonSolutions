class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        n = len(nums)
        num_dict = {}
        for i in xrange(n):
            num = nums[i]
            if num in num_dict:
                j = num_dict[num]
                if i-j<=k:
                    return True
                else:
                    num_dict[num]=i
            else:
                num_dict[num] = i
        return False
        