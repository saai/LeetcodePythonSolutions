class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def findMin(self, nums):
        n = len(nums)
        if n == 0 :
            return 0
        low = 0
        high= n-1
        while(low<high):
            mid = (low+high)/2
            if nums[mid]>nums[high]:
                low = mid+1
            elif nums[mid] == nums[high]:
                high -= 1
            else:
                high = mid
        return nums[low]