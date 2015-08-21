class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        path = []
        self.dfs(k,n,res,path,1,9)
        return res
        
    def dfs(self, k, n, res, path, start,end):
        if k == 0 and n != 0: # target is not reached , but the count is 0
            return 
        if k == 0 and n == 0: # bingo
                res.append(path[:])
        if n < k: #the needed number count is larger than target.
            return 
        if k>(end-start)+1: # the rest count is less than needed count
            return 
        while(start<=end):
            path.append(start)
            self.dfs(k-1,n-start,res,path,start+1,end)
            path.pop()
            start +=1