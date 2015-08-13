class Solution:
    # @param {character[][]} board
    # @param {string} word
    # @return {boolean}
    def exist(self, board, word):
        nr = len(board)
        nc = len(board[0])
        m = len(word)
        isVisited = [[False for i in xrange(nc)] for j in xrange(nr)]
        def dfs(p,i,j):
            if p == m:
                return True
            if i >= nr or i<0:
                return False
            if j >=nc or j <0:
                return False
            if board[i][j] != word[p] or isVisited[i][j]:
                return False
            isVisited[i][j] = True
            res = dfs(p+1,i-1,j) or dfs(p+1,i+1,j) or dfs(p+1,i,j-1) or dfs(p+1,i,j+1)
            isVisited[i][j] = False
            return res
        for i in xrange(nr):
            for j in xrange(nc):
                    res = dfs(0,i,j)
                    if res:
                        return True
        return False