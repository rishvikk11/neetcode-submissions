class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        if len(nums) % 2 == 1:
            return False
        nums.sort()

        for n in nums:
            a = nums.pop()
            b = nums.pop()

            if a != b:
                return False

        return True