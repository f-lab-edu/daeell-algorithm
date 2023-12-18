class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        l, r = 0, len(s) - 1
        s = list(s)

        while l < r:  # O(n)은 len(s)
            while l < r and s[l] not in vowels:  # O(vowels)
                l += 1
            while l < r and s[r] not in vowels:  # O(vowels)
                r -= 1

            s[l], s[r] = s[r], s[l]  # O(1)
            l += 1
            r -= 1

        return "".join(s)  # O(n)
    
# 12/18 set을 활용하여 검색 속도 최적화

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])
        l, r = 0, len(s) - 1
        s = list(s)

        while l < r:  # O(n)은 len(s)
            while l < r and s[l] not in vowels:  # O(1)
                l += 1
            while l < r and s[r] not in vowels:  # O(1)
                r -= 1

            s[l], s[r] = s[r], s[l]  # O(1)
            l += 1
            r -= 1

        return "".join(s)  # O(n)