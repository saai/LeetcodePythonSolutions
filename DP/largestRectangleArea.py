class Solution:
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