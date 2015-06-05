class Solution:
	def permuteUnique(self, nums):
        if nums==None:
            return None
        if len(nums)==0:
            return None
        if len(nums)==1:
            return [nums,]
        first=nums[0]
        result=[]
        reduce_nums=nums[1:]
        perm_result = self.permuteUnique(reduce_nums)
        for i in range(0,len(perm_result)):
            for j in range(0, len(perm_result[i])+1):
                if (j-1>=0)&(first==perm_result[i][j-1]):
                   continue
                perm=[it for it in perm_result[i]]
                perm.insert(j,first)
                if perm not in result:
                    result.append(perm)
        return result