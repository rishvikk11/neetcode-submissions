class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False; 
        if(set(s) != set(t)): 
            return False 
        count = defaultdict(int)
        for i in range(len(s)): 
            count[s[i]] += 1
            count[t[i]] += 1 

        for key in count: 
            if(count[key] % 2 != 0): 
                return False 
            
        return True 
 
        