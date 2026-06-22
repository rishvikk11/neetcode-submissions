"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        days = max_days = 0
        intervals.sort(key=lambda x:(x.start))
        recentEnd = intervals[0].end
        i = 0
        
        for interval in intervals:
            print((interval.start, interval.end))
            if interval.start < recentEnd:
                days += 1
                max_days = max(days, max_days)
                recentEnd = min(recentEnd, interval.end)
            else:
                i += 1
                recentEnd = min(interval.end, intervals[i].end)
        return max_days 
        