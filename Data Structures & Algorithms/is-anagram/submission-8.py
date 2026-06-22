class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = defaultdict(int)
        tDict = defaultdict(int)

        for c in s: 
            sDict[c] += 1
        
        for c in t:
            tDict[c] += 1

        if sDict != tDict:
            return False
        return True