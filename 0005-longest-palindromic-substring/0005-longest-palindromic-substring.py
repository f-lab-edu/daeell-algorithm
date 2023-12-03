class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(l, r):
            while(l >= 0 and r < len(s) and s[l] == s[r]):
                l -= 1
                r += 1
            return s[l+1:r]
        
        res = ""
        for i in range(len(s)):
            odd = check(i, i)
            even = check(i, i+1)
            
            if len(odd) > len(res):
                res = odd
            if len(even) > len(res):
                res = even
        return res