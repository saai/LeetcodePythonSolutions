class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        nr = len(dungeon)
        nc = len(dungeon[0])
        a = [[sys.maxint for j in xrange(nc+1)] for j in xrange(nr+1)]
        a[nr][nc-1] = 1
        a[nr-1][nc] = 1
        for i in range(nr-1,-1,-1):
            for j in range(nc-1,-1,-1):
                need = min(a[i][j+1] , a[i+1][j]) - dungeon[i][j]
                a[i][j] = 1 if need<=0 else need
        return a[0][0]
        
    def calculateMinimumHP2(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        nr = len(dungeon)
        nc = len(dungeon[0])
        row = [sys.maxint for j in xrange(nc+1)]
        row[nc-1] = 1
        for i in range(nr-1,-1,-1):
            right = sys.maxint
            for j in range(nc-1,-1,-1):
                need = min(right, row[j]) - dungeon[i][j]
                row[j+1] = right
                right = 1 if need<= 0 else need
            row[0] = right
        return row[0]
        
        