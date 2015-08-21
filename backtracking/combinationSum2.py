class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        path = []
        res = []
        candidates.sort()
        def dfs(i,n,t):
            if t == 0:
                res.append(path[:])
            while(i<n and candidates[i]<=t):
                path.append(candidates[i])
                dfs(i+1,n,t-candidates[i])
                path.pop()
                i += 1
                while(i<n and candidates[i]==candidates[i-1]):
                    i += 1
        dfs(0,len(candidates),target)
        return res