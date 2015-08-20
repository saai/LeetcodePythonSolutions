# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param {Interval[]} intervals
    # @return {Interval[]}
    def merge(self, intervals):
        res = []
        # self.qsortIntervals(intervals, 0, len(intervals-1))
        for i in sorted(intervals,key=lambda i : i.start):
            if res and i.start <= res[-1].end:
                res[-1].end = max(i.end, res[-1].end)
            else:
                res.append(i)
        return res
                
    def qsortIntervals(self,intervals,l,r):
        if l>=r:
            return 
        i = l 
        j = r
        pivot = intervals[(l+r)/2].start
        while(i<=j):
            while(i<=j and intervals[i].start < pivot):
                i += 1
            while(j>=i and intervals[j].start > pivot):
                j -= 1
            if i<=j:
                t = intervals[i]
                intervals[i] = intervals[j]
                intervals[j] = t
                i += 1
                j -= 1
        if j>l:
            self.qsortIntervals(intervals,l,j)
        if i<r:
            self.qsortIntervals(intervals,i,r)
