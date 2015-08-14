class Solution:
    # @param {integer} numRows
    # @return {integer[][]}
    def generate(self, numRows):
        res = []
        row = []
        for i in range(0,numRows):
            n = len(row)
            row =[1]+[row[j-1] + (row[j] if j<n else 0) for j in range(1,n+1)]
            res.append(row)
        return res
            