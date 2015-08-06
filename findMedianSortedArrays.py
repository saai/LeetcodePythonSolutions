class Solution:   
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):
        m,n = len(nums1),len(nums2)
        if m == 0 and n == 0:
            return 0
        elif m == 0 :
            mid = n/2
            if n%2: #odd
                return nums2[mid]
            else:
                return (nums2[mid-1]+nums2[mid])/2.0
        elif n == 0:
            mid = m/2
            if m%2: #odd
                return nums1[mid]
            else:
                return (nums1[mid-1]+nums1[mid])/2.0
        mid = (m+n)/2
        p1 = 0
        p2 = 0
        while(p1<=mid and p2 < n):
            if p1 >=len(nums1):
                nums1.append(nums2[p2])
                p2+=1
                p1+=1
            else:
                if nums2[p2]<=nums1[p1]:
                    nums1.insert(p1,nums2[p2])
                    p2+=1
                    p1+=1
                else:
                    p1+=1
        if (m+n)%2: # odd
            return nums1[mid]
        else: #even
            return (nums1[mid-1]+nums1[mid])/2.0
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays2(self, nums1, nums2):
        m,n = len(nums1),len(nums2)
        if m == 0 and n == 0:
            return 0
        elif m == 0 :
            mid = n/2
            if n%2: #odd
                return nums2[mid]
            else:
                return (nums2[mid-1]+nums2[mid])/2.0
        elif n == 0:
            mid = m/2
            if m%2: #odd
                return nums1[mid]
            else:
                return (nums1[mid-1]+nums1[mid])/2.0
        mid = (m+n)/2
        p2 = 0
        p1 = 0
        while(p1<=mid and p2 < n):
            target = nums2[p2]
            if p1 >= len(nums1):
                nums1 += nums2[p2:]
                break
            else:
                idx = self.bsindex(nums1[p1:],target)
                p1 = p1 + idx  
                if p1 >= len(nums1):
                    nums1+=nums2[p2:]
                    break
                else:
                    nums1.insert(p1, target)
                p2 += 1
                p1 += 1 
        if (m+n)%2: # odd
            return nums1[mid]
        else: #even
            return (nums1[mid-1]+nums1[mid])/2.0
    def bsindex(self, nums,target):
        n = len(nums)
        low = 0
        high = n-1
        while(low<=high):
            if target <=nums[low]:
                return low
            if target >= nums[high]:
                return high + 1
            mid = (low+high)/2
            if nums[mid] == target:
                return mid + 1
            elif nums[mid]>target:
                high = mid-1
            else:
                low = mid + 1
        return low 
            