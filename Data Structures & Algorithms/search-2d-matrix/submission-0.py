class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # one approach is that we can binary search our way into finding the row the target value is in, then after finding the row, we binary search our way into finding the value in the row
        rows, cols = len(matrix), len(matrix[0])
        top, bot = 0, rows-1

        while top <= bot:
            m = (top+bot) // 2
            if target < matrix[m][0]:
                bot = m-1
            elif target > matrix[m][cols-1]:
                top = m+1
            else:
                break
        
        if not (top <= bot):
            return False
        
        l,r = 0,cols-1
        while l <= r:
            mid = (l+r) // 2
            if target < matrix[m][mid]:
                r = mid-1
            elif target > matrix[m][mid]:
                l = mid+1
            else:
                return True
        return False
