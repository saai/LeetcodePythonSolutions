class Solution:
    # @param {integer} n
    # @return {string[]}
    def generateParenthesis(self, n):
        res = []
        def dfs(res,s, n, m):
            if n == 0 and m == 0:
                res.append(s)
                return 
            if m > 0:
                dfs(res,s+')',n,m-1)
            if n > 0:
                dfs(res,s+'(',n-1,m+1)
        dfs(res,'',n,0)
        return res