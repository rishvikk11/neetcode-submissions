class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # area is defined by its width and height, we need to find an optimal point where we can maximize our area
        # start by maximizing width and slowly compromising width for larger height to find optimal point
        maxArea = 0
        l,r = 0, len(heights)-1

        while l < r:
            maxArea = max(maxArea, (r-l) * min(heights[l], heights[r]))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return maxArea