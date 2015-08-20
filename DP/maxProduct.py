cclass Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxProduct(self, nums):
        n = len(nums)
        max_p = nums[0]
        cur_max_p = nums[0]
        cur_min_p = nums[0]
        for i in range(1,n):
            pre_max_p = cur_max_p
            if pre_max_p*nums[i]<=0:
                cur_max_p = max(cur_min_p*nums[i],nums[i])
            else:
                cur_max_p = max(pre_max_p*nums[i],cur_min_p*nums[i])
            cur_min_p = min(pre_max_p*nums[i],cur_min_p*nums[i],nums[i])
            if max_p < cur_max_p:
                max_p = cur_max_p
        return max_p