from heapq import *
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        skyline = []
        i = 0
        n = len(buildings)
        liveHR = []
        while(i<n or liveHR):
            print liveHR 
            if not liveHR or i<n and buildings[i][0] <= -liveHR[0][1]:
                x = buildings[i][0]
                while(i<n and buildings[i][0] == x):
                    heappush(liveHR,(-buildings[i][2],-buildings[i][1])) # compare first element, else second element , in order.
                    i += 1
            else:
                x = -liveHR[0][1]
                while(liveHR and -liveHR[0][1] <= x):
                    heappop(liveHR) # after pop the liveHR[0][0] will be the smallest .
            height = len(liveHR) and -liveHR[0][0]
            if not skyline or height != skyline[-1][1]:
                skyline.append([x,height])
                print x,height
        return skyline