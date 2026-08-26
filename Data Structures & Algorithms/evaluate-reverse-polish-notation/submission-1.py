class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        if tokens[0] == '+' or tokens[0] == '-' or tokens[0] == '*' or tokens[0] == '/':
            return 0
        
        ops = ["+", "*", "-", "/"]
        for t in tokens:
            if t in ops:
                val2 = int(stack.pop())
                val1 = int(stack.pop())
                if t == "+":
                    stack.append(val1+val2)
                if t == "*":
                    stack.append(val1*val2)
                if t == "-":
                    stack.append(val1-val2)
                if t == "/":
                    stack.append(val1/val2)
            else:
                stack.append(t)

        return int(stack[-1])

