# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        n = len(intervals)
        i = 0       
        while(i<n and newInterval.start > intervals[i].end):
            i += 1
        while(i<len(intervals) and newInterval.end>=intervals[i].start):
            newInterval.start = min(intervals[i].start, newInterval.start)
            newInterval.end = max(intervals[i].end, newInterval.end)
            intervals.pop(i)
        intervals.insert(i,newInterval)
        return intervals
        