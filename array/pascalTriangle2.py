class Solution:
    # @param {integer} rowIndex
    # @return {integer[]}
    def getRow(self, rowIndex):
        row = []
        for i in range(0,rowIndex+1):
            n = len(row)
            row = [1]+[row[j-1] + (row[j] if j < n else 0) for j in range(1,n+1)]
        return row