class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        for i in range(1, n + 1):
            res[i] = res[i >> 1] + (i & 1)
        return res

# 12/19 top - down
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = {0: 0}

        def count_bits_top_down(num):
            if num in res:
                return res[num]
            tmp = count_bits_top_down(num >> 1) + (num & 1)
            res[num] = tmp
            return tmp

        for i in range(n, -1, -1):
            count_bits_top_down(i)

        return [res[i] for i in range(n + 1)]