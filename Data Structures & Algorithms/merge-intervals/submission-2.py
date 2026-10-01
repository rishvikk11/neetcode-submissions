class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort the intervals by start time
        # if the current meeting's start time is less than or equal to the last meeting's end time, we merge
        merged = []
        intervals.sort(key = lambda x: x[0])

        for interval in intervals:
            # if there's no overlap
            if not merged or interval[0] > merged[-1][1]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged