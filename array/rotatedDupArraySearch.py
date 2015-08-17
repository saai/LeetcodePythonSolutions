class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        n = len(nums)
        if n == 0:
            return False
        l = 0
        r = n-1
        if l == r and target != nums[l]:
            return False
        if target == nums[l] or target == nums[r]:
            return True
        mid = r/2
        if target == nums[mid]:
            return True
        if nums[mid]<nums[r]: #right ordered 
            if target>nums[mid] and target<nums[r]: # binary search in right array
                return self.bsearch(nums[mid+1:],target)
            else:
                return self.search(nums[:mid],target) # left disorder search
        elif nums[mid]>nums[l]: # left ordered
            if target<nums[mid] and target>nums[l]: # binary search in left array
                return self.bsearch(nums[:mid],target)
            else:
                return self.search(nums[mid+1:],target)
        else:
            return self.search(nums[:mid],target) or self.search(nums[mid+1:],target)

    def bsearch(self, nums,target):
        n = len(nums)
        l = 0
        r = n-1
        while(l<=r):
            mid = (l+r)/2
            if target == nums[mid]:
                return True
            elif target > nums[mid]:
                l= mid + 1
            else:
                r= mid -1
        return False
