class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # key = number, value = index
        last_seen = {}

        for r in range(len(nums)):
            if nums[r] in last_seen and r - last_seen[nums[r]] <= k:
                return True
            last_seen[nums[r]] = r
        
        return False



