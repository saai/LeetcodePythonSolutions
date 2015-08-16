class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsetsWithDup(self, nums):
        res = [[]]    
        nums.sort()
        for num in nums:
            temp = []
            for ans in res:
                l = ans + [num]
                if l not in res:
                    temp.append(l)
            res.extend(temp)
        return res