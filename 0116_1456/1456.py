class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        max_cnt, cnt = 0, 0

        for word in s[:k]:
            if word in vowels:
                cnt += 1

        max_cnt = cnt

        for i in range(k, len(s)):
            if s[i] in vowels:
                cnt += 1
            if s[i - k] in vowels:
                cnt -= 1
            max_cnt = max(cnt, max_cnt)

        return max_cnt
