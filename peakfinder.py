class Solution:
    # @param nums, an integer[]
    # @return an integer
    def findPeakElement1(self, nums): #o(n)
        l = len(nums)
        for i in xrange(l):
            if i==l-1:
                return i
            elif i==0 :
                if nums[i]>nums[i+1]:
                    return i
            elif nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                return i 
     def findPeakElement2(self, nums): #o(log n)
        l = len(nums)
        if l == 0:
            return 
        low,high = 0,l-1
        while (low<=high):
            if low == high:
                return low
            mid = (low+high)/2
            if nums[mid]<nums[mid+1]:
                low = mid+1
            else:
                high = mid
        return mid