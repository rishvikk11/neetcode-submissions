class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_len = len(s1)
        countOne, countTwo = {}, {}
        for i in range(len(s1)):
            countOne[s1[i]] = 1 + countOne.get(s1[i], 0)
        
        l = 0
        for j in range(len(s2)):
            countTwo[s2[j]] = 1 + countTwo.get(s2[j], 0)
            print(countTwo)
            if j-l+1 == window_len:
                if countTwo == countOne:
                    return True
                countTwo[s2[l]] -= 1
                if countTwo[s2[l]] == 0:
                    del countTwo[s2[l]]
                l += 1
        
        return False
