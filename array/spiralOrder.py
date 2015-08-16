class Solution:
    # @param {integer[][]} matrix
    # @return {integer[]}
    def spiralOrder(self, matrix):
        res = []
        nr = len(matrix)
        if nr == 0:
            return res
        nc = len(matrix[0])
        min_j = 0
        max_j = nc-1
        min_i = 0
        max_i = nr-1
        while (min_i <= max_i and min_j <= max_j):
            # go right
            for j in range(min_j,max_j+1):
                res.append(matrix[min_i][j])
            min_i += 1
            # go down
            for i in range(min_i,max_i+1):
                print i
                res.append(matrix[i][max_j])
            max_j -= 1
            if max_i >= min_i:
                # go left 
                for j in range(max_j,min_j-1,-1):
                    print j
                    res.append(matrix[max_i][j])
                max_i -= 1
            if max_j >= min_j:
                # go up
                for i in range(max_i,min_i-1,-1):
                    res.append(matrix[i][min_j])
                min_j += 1
        return res
            