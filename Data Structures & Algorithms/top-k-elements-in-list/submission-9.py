class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        freqs = [[] for _ in range(len(nums)+1)]

        for n in nums:
            counts[n] += 1

        for num, freq in counts.items():
            freqs[freq].append(num)

        res = []
        for i in range(len(freqs)-1, -1, -1):
            res.extend(freqs[i])
            if len(res) == k:
                return res
