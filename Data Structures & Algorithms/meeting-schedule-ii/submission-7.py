"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Split interval into start and end times and add each time into one array
        times = []
        for interval in intervals:
            times.append((interval.start, 1))
            times.append((interval.end, -1))
        
        # Sort the times array from least to greatest
        times.sort()

        # Track a max-active amt of rooms required to schedule meetings
        max_active = 0
        active = 0
        for time in times:
            active += time[1]
            max_active = max(active, max_active)
        
        return max_active
        

    