class Solution:
    # @param {integer[]} nums1
    # @param {integer} m
    # @param {integer[]} nums2
    # @param {integer} n
    # @return {void} Do not return anything, modify nums1 in-place instead.
    def merge(self, nums1, m, nums2, n):
        p1 = m-1
        p2 = n-1
        p3 = m+n-1
        while(p1>=0 and p2>=0):
            if nums1[p1]>nums2[p2]:
                nums1[p3] = nums1[p1]
                p1 -= 1
            else:
                nums1[p3] = nums2[p2]
                p2 -= 1
            p3 -= 1
        while (p2>=0):
            nums1[p3] = nums2[p2]
            p3 -= 1
            p2 -= 1