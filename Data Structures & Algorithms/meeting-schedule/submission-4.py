"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        active = max_active = 0
        intervals.sort(key=lambda x: x.start)
        recentEnd = intervals[0].end
        for interval in intervals: 
            if interval.start < recentEnd: 
                active += 1
                max_active = max(active, max_active)
            else:
                recentEnd = interval.end
        return max_active == 1


