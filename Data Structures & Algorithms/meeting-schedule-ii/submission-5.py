"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
       times = []
       for interval in intervals:
          times.append((interval.start, 1))
          times.append((interval.end, -1))
    
       times.sort(key=lambda x: (x[0], x[1]))
       res = max_res = 0
       for time in times:
          res += time[1]
          max_res = max(max_res, res)

       return max_res 
    


