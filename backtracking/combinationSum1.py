class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        path = []
        candidates.sort()
        def dfs(i,n,t):
            if t == 0:
                res.append(path[:])
                return
            while(i< n and candidates[i]<=t):
                path.append(candidates[i])
                dfs(i,n,t-candidates[i])
                path.pop()
                i += 1
        dfs(0,len(candidates),target)
        return res

        