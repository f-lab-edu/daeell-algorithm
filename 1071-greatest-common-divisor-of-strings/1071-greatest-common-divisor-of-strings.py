from math import gcd
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        gcd_len = gcd(len(str1), len(str2))
        
        base = str1[:gcd_len]
        if str1 == base * (len(str1) // gcd_len) and str2 == base * (len(str2) // gcd_len):
            return base
        return ""