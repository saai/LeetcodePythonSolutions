class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        nQueens = [['.' for i in xrange(n)] for i in xrange(n)]
        res = []
        flag = [1]*(5*n-2)
        self.solveNQueensHelper(res, nQueens, flag, 0,n)
        return res
    def solveNQueensHelper(self, res, nQueens, flag, row, n):
        if row == n:
            res.append([''.join(r) for r in nQueens])
        for col in xrange(n):
            if flag[col] and flag[n+col+row] and flag[4*n-2 + col - row]:
                flag[col] = flag[n+col+row] = flag[4*n-2 + col - row] = 0
                nQueens[row][col] = 'Q'
                self.solveNQueensHelper(res, nQueens, flag, row+1, n)
                nQueens[row][col] = '.'
                flag[col] = flag[n+col+row] = flag[4*n-2 + col - row] = 1
            
        
            