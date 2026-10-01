"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # sort all intervals by their start time
        # if there's overlap, return false, otherwise we're good to go
        if not intervals:
            return True

        intervals.sort(key = lambda x: x.start)
        last_meeting = intervals[0]

        for interval in intervals[1:]:
            if interval.start < last_meeting.end:
                return False
            else:
                last_meeting = interval

        return True