class Solution:
	def numTrees(self, n):
        if n == 0 : 
            return 0
        if n == 1:
            return 1
        c = [0,1]
        for i in range(2,n+1):
            count_ci = 0
            for j in range(0,i):
                l = j
                r = i-j-1
                if c[l]!=0 and c[r]!=0:
                    count_ci += c[l]*c[r]
                else:
                    count_ci += c[l]+c[r]
            c.append(count_ci)
                
        return c[n]
    