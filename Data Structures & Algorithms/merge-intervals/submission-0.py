class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        left = intervals[0]
        res = []
        for interval in intervals[1:]:
            if interval[0] <= left[1]:
                left[1] = max(left[1], interval[1])
            else:
                res.append(left)
                left = interval
        res.append(left)
        return res