class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        path = []
        self.combineHelper(n,k,path,res)
        return res
    def combineHelper(self, n, k, path, res):
        if k == 0:
            res.append(path[::-1])
        for i in range(n, 0, -1):
            path.append(i)
            self.combineHelper(i-1,k-1,path, res)
            path.pop()
        