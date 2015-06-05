class Solution:
	def numDistinct(self, s, t):
        m = len(t)
        n = len(s)
        #init mem matrix
        mem = []
        for i in range(0,m+1):
            row = []
            for j in range(0,n+1):
                row.append(0)
            mem.append(row)
        #set first line
        for j in range(0,n+1):
            mem[0][j] = 1
        for i in range(0,m):
            for j in range(0,n):
                if s[j]==t[i]:
                    mem[i+1][j+1] = mem[i+1][j] + mem[i][j]
                else:
                    mem[i+1][j+1] = mem[i+1][j]
        return mem[m][n]