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
    
# 12/24
class Solution:
    def convert(self, s: str, n: int) -> str:
        if n == 1:
            return s

        res = ""
        for r in range(n):
            inc = 2 * (n - 1)
            for i in range(r, len(s), inc):
                res += s[i]
                mid = i + inc - 2 * r
                if r != 0 and r != n - 1 and mid < len(s):
                    res += s[mid]

        return res