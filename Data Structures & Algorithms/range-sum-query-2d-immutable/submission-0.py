class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # at (i,j), the prefix sum will be the sum of the entire rectangle from (0,0) to (i,j)
        # 2d prefix sum matrix, where prefix[i][j] = matrix[i][j] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]
        rows, cols = len(matrix), len(matrix[0])
        self.prefix_sums = [[0] * (cols + 1) for r in range(rows + 1)]

        for r in range(1, rows+1):
            for c in range(1, cols+1):
                self.prefix_sums[r][c] = matrix[r-1][c-1] + self.prefix_sums[r-1][c] + self.prefix_sums[r][c-1] - self.prefix_sums[r-1][c-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # update the rows and cols to match the offset of 2d prefix sum
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1

        bottomRight = self.prefix_sums[row2][col2]
        top = self.prefix_sums[row1-1][col2]
        left = self.prefix_sums[row2][col1-1]
        topLeft = self.prefix_sums[row1-1][col1-1]

        return bottomRight - top - left + topLeft


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)