class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permute(self, nums):
        nums.sort()
        n = len(nums)
        res = []
        cur_nums = nums[:]
        v = True
        while(v):
            res.append(cur_nums[:])
            v = self.nextPermutation(cur_nums)
        return res
        
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def nextPermutation(self, nums):
        n = len(nums)
        last = 0    
        for i in range(1,n):
            if nums[i-1]<nums[i]:
                last = i
        if last == 0:
            return False
        else:
            first = nums[last-1] 
            head = n-1
            while(head >last and nums[head]<=first):
                head -= 1
            nums[last-1] = nums[head]
            nums[head] = first
            # reverse the array except first element
            for i in range(0,(n-last)/2):
                t = nums[i+last]
                nums[i+last] = nums[n-1-i]
                nums[n-1-i] = t
            return True         
            