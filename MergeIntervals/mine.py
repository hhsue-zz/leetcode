#!/usr/bin/python


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
         self.start = s
         self.end = e

# compare (1,4),(4,6),(3,5)
# if lower bound is lower than yours, and if my upper is higher than your lower, take my lower, and the highest higher
class Solution:
    # @param {Interval[]} intervals
    # @return {Interval[]}
    result_intervals = intervals
    def merge(self, intervals):
        for i in range(len(intervals)-1):
            for j in range(i,len(intervals)-1):
                if intervals[j][0] < intervals[j+1][0]
                    if intervals[j][1] > intervals[j+1][0]:
                        
            

#[1,3],[2,6],[8,10],[15,18]
a = Interval(1,3)
b = Interval(2,6)
c = Interval(8,10)
d = Interval(15,18)

intervals = [a,b,c,d]

s = Solution()
print s.merge(intervals)
