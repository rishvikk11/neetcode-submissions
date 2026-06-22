class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''mapping = defaultdict(int)
        for n in nums:
            mapping[n] += 1
            if mapping[n] > 1:
                return True
        
        return False '''

        seen = set()
        for n in nums: 
            if n in seen:
                return True
            seen.add(n)
        
        return False