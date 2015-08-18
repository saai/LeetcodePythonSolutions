class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        nr = len(matrix)
        nc = len(matrix[0])
        for row in matrix:
            lo = 0 
            hi = nc-1
            if target < row[lo]:
                break
            elif target > row[hi]:
                continue
            while(lo<=hi):
                mid = (lo+hi)/2
                if target == row[mid]:
                    return True
                elif target > row[mid]:
                    lo = mid + 1
                else:
                    hi = mid-1
        return False
