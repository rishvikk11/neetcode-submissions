class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        remove = 0

        for i in range(1, len(intervals)):
            prev = intervals[i-1]
            curr = intervals[i]

            if curr[0] < prev[1]:
                remove += 1
                curr[1] = min(curr[1], prev[1])

        return remove