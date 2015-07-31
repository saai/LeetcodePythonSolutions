class Solution:
    # @param {string} s
    # @return {string[][]}
    def partition(self, s):
        res = []
        self.dfs(s,[],res)
        return res
    def dfs(self,s,path,res):
        if not s :
            res.append(path[:])
            return
        for i in xrange(1,len(s)+1):
            if self.isPal(s[:i]):
                path.append(s[:i])
                self.dfs(s[i:],path,res)
                path.pop()
            
    def isPal(self, s):
        return s == s[::-1]
            
        