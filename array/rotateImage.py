class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
        n = len(matrix)
        n = len(matrix[0])
        # transpose
        for i in range(0,n):
            for j in range(i+1,n):
                t = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = t
            
        #middle symmetric
        mid = n/2 
        for i in range(0,mid):
            j = n-1-i
            for p in range(0,n):
                t = matrix[p][i]
                matrix[p][i] = matrix[p][j]
                matrix[p][j] = t
