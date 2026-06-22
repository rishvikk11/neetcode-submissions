class Solution:
    def isValid(self, s: str) -> bool:
        opStack = []
        for c in s: 
            match c: 
                case '(':
                    opStack.append(c)
                case '{':
                    opStack.append(c)
                case '[':
                    opStack.append(c)
                case ')':
                    if len(opStack) > 0 and opStack[-1] == '(':
                        opStack.pop()
                    else: 
                        return False
                case '}':
                    if len(opStack) > 0 and opStack[-1] == '{':
                        opStack.pop()
                    else: 
                        return False
                case ']':
                    if len(opStack) > 0 and opStack[-1] == '[':
                        opStack.pop()
                    else:
                        return False
                
        return len(opStack) == 0

        