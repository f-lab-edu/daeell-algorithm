class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxV = max(candies)
        return [candy + extraCandies >= maxV for candy in candies]