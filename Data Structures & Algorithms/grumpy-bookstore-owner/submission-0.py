class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        l = 0
        base = sum(customers[r] for r in range(len(grumpy)) if grumpy[r] == 0)
        max_window = 0
        curr_window = 0

        for r in range(len(grumpy)):
            if grumpy[r] == 1:
                curr_window += customers[r]
            
            if r-l+1 == minutes:
                max_window = max(max_window, curr_window)
                if grumpy[l] == 1:
                    curr_window -= customers[l]
                l += 1

        return base + max_window