class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # dynamic sliding window problem
        window = set()
        l = 0

        for r in range(len(nums)):
            # fix window size
            if r - l > k:
                window.remove(nums[l])
                l += 1
            if nums[r] in window:
                return True
            window.add(nums[r])
        
        return False



