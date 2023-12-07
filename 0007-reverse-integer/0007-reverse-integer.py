class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX, INT_MIN = 2**31 -1, -2**31
        is_minus = x < 0
        reversed_num = 0
        x = abs(x)
        while x > 0:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10
            if reversed_num > INT_MAX or reversed_num < INT_MIN:
                return 0
        return -reversed_num if is_minus else reversed_num