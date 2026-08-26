class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total, rows = 0, len(mat)
        for r in range(rows):
            total += mat[r][r]
            total += mat[r][rows - r - 1]
        
        if rows % 2 == 1:
            total -= mat[rows // 2][rows // 2]
        return total
