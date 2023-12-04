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
    
# 12/5 피드백 적용
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def getMaximumPalindrome(l, r):
            while(l >= 0 and r < len(s) and s[l] == s[r]):
                l -= 1
                r += 1
            return s[l+1:r]
        
        res = ""
        for i in range(len(s)):
            odd = getMaximumPalindrome(i, i)
            even = getMaximumPalindrome(i, i+1)
            
            res = max(odd, even, res, key=len)
        return res