class Solution:
    def reverse(self, s: list, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

    def reverseWords(self, s: str) -> str:
        s = list(s)
        start = 0
        for i in range(len(s)):  # O(n)
            if s[i] == " ":
                self.reverse(s, start, i - 1)  # O(k) k는 해당 단어의 길이
                start = i + 1
        self.reverse(s, start, i)  # O(m) m은 해당 단어의 길이
        self.reverse(s, 0, len(s) - 1)  # O(n)

        return " ".join("".join(s).split())  # O(n)