class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # optimal algorithm: O(N), instead of using two hashmaps, 
        # use a hashmap and an array to avoid needing to sort the frequencies
        numToFreq = defaultdict(int)
        freqs = [[] for i in range(len(nums)+1)]

        for n in nums: 
            numToFreq[n] += 1
        for val, freq in numToFreq.items():
            freqs[freq].append(val)

        res = []
        for i in range(len(freqs)-1, 0, -1):
            res.extend(freqs[i])
            if len(res) == k:
                break

        return res

