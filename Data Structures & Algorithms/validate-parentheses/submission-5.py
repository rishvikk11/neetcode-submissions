class Solution:
    def isValid(self, s: str) -> bool:
        # make a dictionary with all the valid pairings
        mapping = {')': '(', '}': '{', ']': '['}
        # stack to track if the parentheses pairings are valid
        stack = []
        for c in s:
            if stack:
                if c in mapping and stack[-1] == mapping[c]:
                    stack.pop()
                else: 
                    stack.append(c)
            else:
                stack.append(c)
        
        return len(stack) == 0