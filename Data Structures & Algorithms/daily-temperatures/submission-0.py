class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # stores pairs (val, index)

        for i,t in enumerate(temperatures):
            # the current temp is greater than the topmost value in the stack
            # what we do here is that we add our values one by one and handle our cases as we go, so if we find a value greater than our topmost value, we handle it immediately and keep going down the stack to see if we can handle other values
            while stack and t > stack[-1][0]:
                v,ind = stack.pop()
                res[ind] = i - ind
            stack.append((t,i))
        return res
