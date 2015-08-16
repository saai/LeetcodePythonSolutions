class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def sortColors(self, nums):
        n = len(nums)
        p1 = -1 # p1 and before p1 all 0, after p2 all 2
        p2 = n
        i = 0
        while (p1 < p2 and i < p2):
            if nums[i] == 0 :
                p1 += 1
                if p1 == i:
                    i += 1
                else:
                    t = nums[p1]
                    nums[p1] = 0
                    nums[i] = t
            elif nums[i] == 2:
                p2 -= 1
                t = nums[p2]
                nums[p2] = 2
                nums[i] = t
            else:
                i += 1