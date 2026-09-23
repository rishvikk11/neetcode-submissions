class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # imagine the array as a linked list, point each indexed value to nums[index], so that if there is a loop, we know there's a duplicate

        # find collision spot (this can be any random point in the loop)
        slow, fast = 0,0
        while True: # there is guaranteed to be a duplicate
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # mathematically, the start of our loop is the duplicate value and the distance from the very start to the start of the loop is the same as the distance from collision point to the start of the loop
        start = 0
        while True:
            start = nums[start]
            slow = nums[slow]
            if start == slow:
                break

        return slow
