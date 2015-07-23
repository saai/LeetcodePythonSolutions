class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[][]}
    def fourSum(self, nums, target):
        nums.sort()
        hash4 = []
        n = len(nums)
        if n<4:
            return hash4
        i=0
        while(i<n):
            t3 = target - nums[i]
            j = i+1
            while(j<n):
                t2 = t3-nums[j]
                front = j+1
                back = n-1
                while(front<back):
                    two_sum = nums[front]+nums[back]
                    if two_sum <t2:
                        front+=1
                    elif two_sum > t2:
                        back -=1
                    else:
                        quadruplet = [nums[i],nums[j],nums[front],nums[back]]
                        hash4.append(quadruplet)
                        while(front < back and nums[front] == quadruplet[2]):
                            front +=1
                        while(front < back and nums[back] == quadruplet[3]):
                            back -=1
                while(j+1<n and nums[j] == nums[j+1]):
                    j+=1
                j+=1
            while(i+1<n and nums[i] == nums[i+1]):
                i+=1
            i+=1
        return hash4 
                    
        