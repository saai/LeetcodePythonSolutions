class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a string[]
    def wordBreak(self, s, wordDict):
        n = len(s)
        res = []
        chars = ''.join(wordDict)
        for i in xrange(n):
            if s[i] not in chars:
                return res
        lw = s[-1]
        lw_end = False
        for word in wordDict:
            if word[-1] == lw:
                lw_end = True
        if not lw_end:
            return res
        self.dfs(s,[],wordDict,res)
        return res
    def dfs(self, s, path,wordDict,res):
        if not s:
            res.append(' '.join(path[:]))
            return 
        for i in range(1,len(s)+1):
            c = s[:i]
            if c in wordDict:
                path.append(c)
                self.dfs(s[i:],path,wordDict,res)
                path.pop()