class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalSquare(self, matrix):
        nr = len(matrix) #row
        if nr <= 0:
            return 0
        nc = len(matrix[0]) #column
        row = [int(s) for s in matrix[0][:]] #last row
        pre = 0
        cur = 0
        max_p = max(row)
        for i in range(1,nr):
            pre = int(matrix[i][0])
            for j in range(1,nc):
                if matrix[i][j] == '0':
                    cur = 0
                else:
                    cur = min(pre,row[j-1],row[j]) + 1
                row[j-1] = pre
                pre = cur
                max_p = max(cur,max_p)
            row[nc-1] = cur
        return max_p**2
        