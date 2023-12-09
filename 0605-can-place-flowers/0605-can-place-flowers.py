class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        flowerbed = [0] + flowerbed + [0]
        count = 0
        for i in range(1, len(flowerbed) - 1):
            if not flowerbed[i - 1] and not flowerbed[i] and not flowerbed[i + 1]:
                flowerbed[i] = 1
                count += 1
            if count == n:
                return True
        return False