"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sortedIntervals = sorted(intervals, key=lambda x: x.start)
        for i in range(len(sortedIntervals)-1):
            if sortedIntervals[i].end > sortedIntervals[i+1].start:
                return False 
        
        return True


