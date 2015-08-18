class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, nums, target):
        n = len(nums)
        lo = 0
        hi = n-1
        i = -1
        while(lo <= hi):
            mid = (lo+hi)/2
            if target == nums[mid]:
                i = mid 
                break
            elif target > nums[mid]:
                lo = mid + 1
            else:
                hi = mid-1
        if i == -1:
            return [-1,-1]
        else:
            s = e = i
            while(s-1 >= 0 and nums[s-1] == nums[i]):
                s -= 1
            while(e+1 < n and nums[e+1] == nums[i]):
                e += 1
            return [s,e]
                