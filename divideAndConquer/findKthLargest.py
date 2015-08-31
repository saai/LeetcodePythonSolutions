class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        k = len(nums) - k
        lo = 0
        hi = len(nums) -1
        while(lo<hi):
            j = self.partition(nums, lo, hi)
            if j<k:
                lo = j + 1
            elif j > k :
                hi = j - 1
            else:
                break
        return nums[k]
                
    def partition(self, nums, lo, hi):
        i = lo
        j = hi
        pivot = nums[lo]
        while(i<j):
            while(i<hi and nums[i]<=pivot):# i stops when nums[i]>pivot or equals hi
                i += 1
            while(j>lo and nums[j]>=pivot): # j stops when nums[j]<pivot or equals lo
                j -= 1
            if i<j:
                t = nums[i]
                nums[i] = nums[j]
                nums[j] = t
                i += 1
                j -= 1
        t = nums[j]
        nums[j] = pivot
        nums[lo] = t
        return j