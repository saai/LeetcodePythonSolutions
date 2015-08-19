class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def nextPermutation(self, nums):
        n = len(nums)
        last = n-1
        while(last>0 and nums[last-1]>=nums[last]):
            last -= 1
        if last == 0:
            nums.reverse()
        else:
            first = nums[last-1] 
            head = n-1
            while(head >last and nums[head]<=first):
                head -= 1
            nums[last-1] = nums[head]
            nums[head] = first
            # reverse the array except first element
            print nums
            for i in range(0,(n-last)/2):
                t = nums[i+last]
                nums[i+last] = nums[n-1-i]
                nums[n-1-i] = t
            