#!/usr/bin/python
# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
         self.start = s
         self.end = e

class Solution:
    # @param {Interval[]} intervals
    # @return {Interval[]}

    def merge(self, intervals):
        # sort by lower bound in interval
        if len(intervals) == 0:
            return []
        intervals_sorted = sorted(intervals, key=lambda e: e.start)
        # if no intersection, append next interval to a list called merged, otherwise, modify the last interval in merged
        merged = []
        merged.append(intervals_sorted[0])
        for i in intervals_sorted[1:]:
            if merged[-1].start < i.start and merged[-1].end > i.start:
                if merged[-1].end < i.end:
                    merged[-1].end = i.end
            else:
                merged.append(i)
        #for m in merged:
        #    print "%d, %d" % (m.start, m.end)
        return merged

# following is original idea that didn't work
'''
        for i in range(len(intervals)-1):
            for j in range(i,len(intervals)-1):
                if intervals[j][0] < intervals[j+1][0] and intervals[j][1] > intervals[j+1][0]
'''            

#[1,3],[2,6],[8,10],[15,18]
a = Interval(1,3)
b = Interval(2,6)
c = Interval(8,10)
d = Interval(15,18)

intervals = [a,b,c,d]

s = Solution()
s.merge(intervals)
