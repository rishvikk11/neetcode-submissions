class Solution:

    def encode(self, strs: List[str]) -> str:
        combined = ""
        for s in strs: 
            combined += "|" + s
        return combined

    def decode(self, s: str) -> List[str]:
        strs = s.split("|")
        strs.pop(0)
        return strs

