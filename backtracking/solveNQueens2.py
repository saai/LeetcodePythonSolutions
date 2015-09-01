count = 0
class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        global count 
        count = 0
        flag = [1]*(5*n-2)
        def totalNQueensHelper(row):
            if row == n:
                global count 
                count += 1
            for col in xrange(n):
                if flag[col] and flag[n+row+col] and flag[4*n-2 +col-row]:
                    flag[col] = flag[n+col+row] = flag[4*n-2 + col - row] = 0
                    totalNQueensHelper(row+1)
                    flag[col] = flag[n+col+row] = flag[4*n-2 + col - row] = 1
        totalNQueensHelper(0)
        return count
        