"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
       start = [interval.start for interval in intervals]
       end = [interval.end for interval in intervals]

       start.sort()
       end.sort() 
       s = e = 0
       active = max_active = 0

       while s < len(intervals):
          if start[s] < end[e]:
            active += 1
            s += 1
            max_active = max(active, max_active)
          else:
            active -= 1
            e += 1
            
       return max_active 
    


