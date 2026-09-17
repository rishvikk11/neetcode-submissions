class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l, r, max_len = 0, 1, 1
        prev = ""

        while r < len(arr):
            # check for valid cases (comparison of previous two values)
            if arr[r] > arr[r-1] and prev != ">":
                max_len = max(max_len, r-l+1)
                r += 1
                prev = ">"
            elif arr[r] < arr[r-1] and prev != "<":
                max_len = max(max_len, r-l+1)
                r += 1
                prev = "<"
            else:
                # if the two values are equal, we wanna start on the second duplicate value and continue
                # otherwise, we wanna start at the value before the failed turbulence
                r = r + 1 if arr[r] == arr[r-1] else r
                l = r - 1
                prev = ""
        
        return max_len


