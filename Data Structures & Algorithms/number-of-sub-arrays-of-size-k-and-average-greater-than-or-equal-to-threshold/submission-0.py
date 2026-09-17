class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # fixed sliding window solution, given a k value
        l = 0
        currSum = 0
        res = 0

        for r in range(len(arr)):
            currSum += arr[r]
            if r-l+1 == k:
                if currSum / k >= threshold:
                    res += 1
                currSum -= arr[l]
                l += 1
            
        return res