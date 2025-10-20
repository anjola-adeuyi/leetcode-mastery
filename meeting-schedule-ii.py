"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        startTime = []
        endTime = []

        for i in intervals:
            startTime.append(i.start)
            endTime.append(i.end)

        startTime.sort()
        endTime.sort()

        # start = sorted([i.start for i in intervals])
        # end = sorted([i.end for i in intervals])

        res = count = 0
        s = e = 0
        while s < len(intervals):
            if startTime[s] < endTime[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1

            res = max(res, count)

        return res
