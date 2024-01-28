class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        cnt = 0
        for i in range(n):
            for j in range(n):
                if all(grid[i][k] == grid[k][j] for k in range(n)):
                    cnt += 1
        return cnt


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row_repr = [",".join(map(str, row)) for row in grid]
        col_repr = [
            ",".join(map(str, [grid[i][j] for i in range(n)])) for j in range(n)
        ]

        row_count = Counter(row_repr)
        col_count = Counter(col_repr)

        count = sum(row_count[row] * col_count[row] for row in row_count)

        return count
