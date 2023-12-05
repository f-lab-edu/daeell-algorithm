class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        zigzag = [[] for _ in range(numRows)]
        idx = 0
        change = 1
        for x in s:
            zigzag[idx].append(x)
            if idx == numRows-1:
                change = -1
            elif idx == 0:
                change = 1
            idx += change
        return "".join("".join(row) for row in zigzag)