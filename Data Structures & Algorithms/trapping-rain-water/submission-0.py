class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0, len(height)-1
        maxLeft, maxRight = height[l], height[r]
        res = 0
        
        while l < r:
            if maxLeft < maxRight:
                res += max(0, maxLeft - height[l])
                l += 1
                maxLeft = max(maxLeft, height[l])
            else:
                res += max(0, maxRight - height[r])
                r -= 1
                maxRight = max(maxRight, height[r])

        return res