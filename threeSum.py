class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        nums.sort()
        res = []
        n = len(nums)
        i = 0
        while(i<n):
            t2 = 0 - nums[i]
            front = i + 1
            back =  n -1
            while(front < back):
                sum = nums[front] + nums[back]
                if sum < t2:
                    front += 1
                elif sum > t2:
                    back -= 1
                else:
                    tripple = [nums[i],nums[front], nums[back]]
                    while(front < back and nums[front]== tripple[1]):
                        front += 1
                    while(front <back and nums[back] == tripple[2]):
                        back -= 1
                    res.append(tripple)
            while(i+1 < n and nums[i+1] == nums[i]):
                i += 1
            i += 1
        return res
            