class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # pair up position and speed for every car
        stack = [] # (pos, speed)
        for i in range(len(position)):
            stack.append((position[i], speed[i]))
        
        stack.sort(key=lambda x: x[0]) # sorting by position
        fleets = 0
        while stack:
            pos, sp = stack.pop()
            hrs = (target-pos) / sp
            while stack and (((target-stack[-1][0]) / stack[-1][1]) <= hrs):
                stack.pop()
            fleets += 1
        
        return fleets
