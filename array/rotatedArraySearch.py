class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        n = len(nums)
        l= 0
        r = n-1
        rot = 0 # the smallest one's index
        while(l<r):
            mid = (l+r)/2
            if nums[mid]>nums[r]:
                l = mid+1
            else:
                r = mid
        rot = l # l==r
        l = 0 
        r = n-1
        while(l<=r):
            mid = (l+r)/2
            realmid = (mid+rot)%n # map to real mid index
            if target==nums[realmid]: # compare with real mid value
                return realmid
            elif target > nums[realmid]: # if not match ,check right area as normal bsearch, because we compare to real value.
                l = mid + 1
            else:
                r = mid -1
        return -1
                
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def search2(self, nums, target):
        n = len(nums)
        if n == 0:
            return -1
        l = 0
        r = n-1
        if l == r and target != nums[l]:
            return -1
        if target == nums[l]:
            return l
        if target == nums[r]:
            return r
        mid = r/2
        if target == nums[mid]:
            return mid
        if nums[mid]<nums[r]: #right ordered 
            if target>nums[mid] and target<nums[r]: # binary search in right array
                idx = self.bsearch(nums[mid+1:],target)
                if idx == -1:
                    return -1
                else:
                    return mid+1+idx
            else:
                return self.search(nums[:mid],target) # left disorder search
        elif nums[mid]>nums[l]: # left ordered
            if target<nums[mid] and target>nums[l]: # binary search in left array
                return self.bsearch(nums[:mid],target)
            else:
                idx = self.search(nums[mid+1:],target)
                if idx == -1:
                    return -1
                else:
                    return mid+1+idx
        else:
            return -1
    def bsearch(self, nums,target):
        n = len(nums)
        l = 0
        r = n-1
        while(l<=r):
            mid = (l+r)/2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                l= mid + 1
            else:
                r= mid -1
        return -1
