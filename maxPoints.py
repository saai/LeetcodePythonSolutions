# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    # @param {Point[]} points
    # @return {integer}
    def maxPoints(self, points):
        x_equal_lines = {}
        y_equal_lines = {}
        k_equal_lines = {}
        n = len(points)
        if n == 0 :
            return 0
        elif n == 1:
            return 1
        max_num = 0
        for i in xrange(n):
            i_x, i_y = points[i].x, points[i].y
            if i_x not in x_equal_lines:
                x_equal_lines[i_x] = 1 # the count of x_equal_lines
            else:
                x_equal_lines[i_x] += 1
            if i_y not in y_equal_lines:
                y_equal_lines[i_y] = 1 # the count of y_equal_lines
            else:
                y_equal_lines[i_y] += 1
            max_num = max(x_equal_lines[i_x],y_equal_lines[i_y],max_num)
            repeat_node = 0
            for j in range(i+1,n):
                j_x , j_y = points[j].x, points[j].y
                if j_x == i_x or j_y == i_y:
                    if j_x == i_x and j_y == i_y:
                        repeat_node += 1
                else:
                    kij = (j_y- i_y)/float(j_x - i_x)
                    if kij not in k_equal_lines:
                        k_equal_lines[kij] = 2 
                    else:
                        k_equal_lines[kij] += 1 
            for key in k_equal_lines:
                max_num = max(max_num, k_equal_lines[key] + repeat_node)
            k_equal_lines.clear()
        return max_num           
        