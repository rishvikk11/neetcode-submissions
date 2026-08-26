class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = [[] for _ in range(len(nums))]
        freqs = {}
        for n in nums:
            freqs[n] = 1 + freqs.get(n, 0)

        for num, freq in freqs.items():
            count[freq-1].append(num)
        
        res = []
        for i in range(len(count)-1, -1, -1):
            res.extend(count[i])
            if len(res) == k:
                return res