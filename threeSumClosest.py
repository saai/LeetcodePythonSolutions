class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumClosest(self, nums, target):
        nums.sort()
        n = len(nums)
        i = 0
        closest = None
        while(i < n):
            t2 = target - nums[i]
            front = i+1
            back = n-1
            while(front < back):
                sum = nums[front] + nums[back]
                if sum < t2:
                    front += 1
                elif  sum > t2:
                    back -= 1
                else :
                    return target # bingo
                if closest == None:
                    closest = sum + nums[i]
                else:
                    dist = abs(t2 - sum)
                    closest = closest if dist > abs(closest-target) else (sum + nums[i])
            while(i+1 < n and nums[i+1] == nums[i]):
                i += 1
            i += 1
        return closest