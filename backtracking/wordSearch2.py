class Solution:
    # @param {character[][]} board
    # @param {string[]} words
    # @return {string[]}
    def findWords(self, board, words):
        trie = {}
        for word in words:
            t = trie
            for c in word:
                if c not in t:
                    t[c] = {}
                t = t[c]
            t['#'] = '#'

        res = []
        nr = len(board)
        nc = len(board[0])
        isVisited = [[False for j in xrange(nc)] for i in xrange(nr)]
        def dfs(i,j,s,trie,res):
            if '#' in trie and s not in res:
                res.append(s)
            if i >=nr or i < 0 or j >=nc or j < 0:
                return 
            if isVisited[i][j] or board[i][j] not in trie:
                return 
            s += board[i][j]
            isVisited[i][j] = True
            dfs(i-1,j,s,trie[board[i][j]],res)
            dfs(i+1,j,s,trie[board[i][j]],res)
            dfs(i,j-1,s,trie[board[i][j]],res)
            dfs(i,j+1,s,trie[board[i][j]],res)
            isVisited[i][j] = False
        
        for i in xrange(nr):
            for j in xrange(nc):
                dfs(i,j,'',trie,res)
        return res
            