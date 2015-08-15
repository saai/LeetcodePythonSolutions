class Solution:
    # @param {integer[]} height
    # @return {integer}
    def trap(self, height):
        n = len(height)
        i = 0
        j = n-1
        last_h = 0
        res = 0
        while (i<j):
            cur_h = min(height[i],height[j])
            if cur_h > last_h:
                for p in range(i,j):
                    v = height[p]
                    if v >= cur_h:
                        continue
                    elif v > last_h:
                        res += cur_h - v
                    else: #v <= last_h
                        res += cur_h - last_h
                last_h = cur_h
            if height[i]<height[j]:
                i += 1
                while(i<j and height[i-1]>height[i]):
                    i += 1
            else:
                j -= 1
                while(i<j and height[j]<height[j+1]):
                    j -= 1
        return res    
                