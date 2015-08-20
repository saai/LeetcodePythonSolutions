class Solution(object):
    def majorityElement(self, nums): # majority element more than n/2
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 1 
        major = nums[0] # one other elements kills one major , but major num is bigger than the sum of the others.
        for i in range(1,len(nums)):
            if count == 0:
                major = nums[i]
                count += 1
            elif major == nums[i]:
                count += 1
            else:
                count -= 1
        return major
            