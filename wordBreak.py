class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a boolean
    def wordBreak(self, s, wordDict):
        n = len(s)
        if n == 0:
            return True
        res = []
        chars = ''.join(wordDict)
        for i in xrange(n):
            if s[i] not in chars:
                return False
        lw = s[-1]
        lw_end = False
        for word in wordDict:
            if word[-1] == lw:
                lw_end = True
        if not lw_end:
            return False
        return self.dfs(s,[],wordDict, res)
        
    def dfs(self, s, path, wordDict,res):
        if not s :
            res.append(path[:])
            return True
        for i in xrange(1,len(s)+1):
            c = s[:i]
            if c in wordDict:
                path.append(c)
                v = self.dfs(s[i:],path,wordDict,res)
                if v:
                    return True
                path.pop()
        return False
        