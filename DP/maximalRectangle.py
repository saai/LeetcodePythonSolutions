class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalRectangle(self, matrix):
        nr = len(matrix)
        if nr <=0:
            return 0
        nc = len(matrix[0])
        heights = [0 for i in xrange(nc)]
        max_p = 0
        for i in xrange(nr):
            for j in xrange(nc):
                if matrix[i][j] == '0':
                    heights[j] = 0
                else:
                    heights[j] += 1
            temp = self.largestRectangleArea(heights)
            max_p = max(temp, max_p)
        return max_p    
    # @param {integer[]} height
    # @return {integer}
    def largestRectangleArea(self, height):
        n  = len(height)
        ma = 0
        stack = [-1]
        for i in xrange(n):
            while(stack[-1] > -1):
                if height[i]<height[stack[-1]]:
                    top = stack.pop()
                    ma = max(ma, height[top]*(i-1-stack[-1]))
                else:
                    break
            stack.append(i)
        while(stack[-1] != -1):
            top = stack.pop()
            ma = max(ma, height[top]*(n-1-stack[-1]))
        return ma     