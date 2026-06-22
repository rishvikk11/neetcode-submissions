"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        mapping = defaultdict(int)
        for interval in intervals:
            mapping[interval.start] += 1
            mapping[interval.end] -= 1

        days = max_days = 0
        for time in sorted(mapping.keys()):
            days += mapping[time]
            max_days = max(days, max_days)
        return max_days
            