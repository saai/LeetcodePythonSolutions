class Solution:
    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):
        n = len(height)
        if n <=1:
            return 0
        ma = 0
        i = 0
        j = n-1
        while(i<j):
            ma =max(ma, (j-i)*min(height[i],height[j]))
            if height[i]<height[j]:
                i += 1
                while(i < j and height[i-1]>height[i]):
                    i+=1
            else:
                j -= 1
                while(i < j and height[j]<height[j+1]):
                    j -= 1
        return ma
                