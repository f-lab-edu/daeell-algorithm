class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:  # O(1)
            return 0
        elif n == 1 or n == 2:  # O(1)
            return 1
        sequence = [0 for _ in range(n + 1)]  # O(n)
        sequence[1], sequence[2] = 1, 1
        for i in range(3, n + 1):  # O(n)
            sequence[i] = sequence[i - 1] + sequence[i - 2] + sequence[i - 3] # O(1)
        return sequence[n]

# 12/19 추가 풀이
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0: # O(1)
            return 0
        if n == 1 or n == 2: # O(1)
            return 1

        first, second, third = 0, 1, 1
        for i in range(3, n + 1): # O(n)
            next_value = first + second + third # O(1) 매우 큰 수일 경우 O(n)
            first, second, third = second, third, next_value # O(1)

        return third