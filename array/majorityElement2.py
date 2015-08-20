class Solution(object):
    def majorityElement(self, nums): # majority larget than n/3
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        candidate1 = 0
        candidate2 = 0
        count1 = 0
        count2 = 0
        n = len(nums)
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 += 1
            elif count2 == 0:
                candidate2 = num
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        count1 = 0
        count2 = 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
        res = []
        if count1 > n//3:
            res.append(candidate1)
        if count2 > n//3:
            res.append(candidate2)
        return res
        # return [i for i in set([candidate1,candidate2]) if nums.count(i) > n//3] 