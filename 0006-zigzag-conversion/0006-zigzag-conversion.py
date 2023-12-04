class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        zigzag = [[] for _ in range(numRows+1)]
        idx = 1
        change = 1
        for x in s:
            zigzag[idx].append(x)
            if idx == numRows:
                change = -1
            elif idx == 1:
                change = 1
            idx += change
        res = ""
        for i in range(1, numRows+1):
            res += "".join(zigzag[i])
        return res