class Solution:
    def isPalindrome(self, s: str) -> bool:
        forwardString = ""
        backwardString = ""
        for char in s: 
            if char.isalnum(): 
                forwardString += char.lower()

        for i in range(len(s)-1, -1, -1):
            if s[i].isalnum():
                backwardString += s[i].lower()

        return forwardString == backwardString