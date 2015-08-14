class Solution:
    # @param {integer[][]} obstacleGrid
    # @return {integer}
    def uniquePathsWithObstacles(self, obstacleGrid):
        nr = len(obstacleGrid)
        nc = len(obstacleGrid[0])
        row = [0 for i in xrange(nc)] # the row befor 0th row
        row[0] = 1
        for i in range(0,nr):
            if row[0] == 0 or obstacleGrid[i][0] == 1:
                row[0] = 0
            for j in xrange(1,nc):
                if obstacleGrid[i][j] == 1:
                        cur = 0
                else:
                    cur = row[j-1]+row[j]
                row[j] = cur
        return row[nc-1]