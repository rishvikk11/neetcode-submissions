class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # very similar to two sum when you rearrange the equation
        prefix = 0
        prefixSums = defaultdict(int) # stores freqs of seen prefix sums
        prefixSums[0] = 1

        # prefix[right] - prefix[left-1] = k
        # prefix[right] - k = prefix[left-1]
        res = 0
        for n in nums:
            prefix += n
            if prefix - k in prefixSums:
                res += prefixSums[prefix-k]
            prefixSums[prefix] += 1

        return res