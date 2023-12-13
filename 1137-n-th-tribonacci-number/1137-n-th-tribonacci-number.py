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