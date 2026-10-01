class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # create a separate merged array
        # append all intervals that don't need any merging prior to our newInterval
        # once we reach a merging point, we need to see how it long there needs to be merging and add it to the merged array
        # then, we just add in the rest of the intervals after
        merged = []
        i = 0
        n = len(intervals)

        while i < n and intervals[i][1] < newInterval[0]:
            merged.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= newInterval[1]:
            i_min = min(intervals[i][0], newInterval[0])
            i_max = max(intervals[i][1], newInterval[1])
            newInterval = [i_min, i_max]
            i += 1
        merged.append(newInterval)

        while i < n:
            merged.append(intervals[i])
            i += 1

        return merged
        