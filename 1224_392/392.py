class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sp_1, sp_2 = 0, 0

        while sp_1 < len(s) and sp_2 < len(t):
            if s[sp_1] == t[sp_2]:
                sp_1 += 1
            sp_2 += 1

        if sp_1 == len(s):
            return True

        return False