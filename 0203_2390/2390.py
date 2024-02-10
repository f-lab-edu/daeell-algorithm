class Solution:
    def removeStars(self, s: str) -> str:
        stk = []

        for c in s:
            if not stk or c is not "*":
                stk.append(c)
            else:
                stk.pop()

        return "".join(stk)


class Solution:
    def removeStars(self, s: str) -> str:
        chars = list(s)
        write = 0

        for read in range(len(chars)):
            if chars[read] != "*":
                chars[write] = chars[read]
                write += 1
            else:
                write -= 1

        return "".join(chars[:write])
