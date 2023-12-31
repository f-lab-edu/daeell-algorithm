class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        now = 0
        highest = 0
        for altitude in gain:
            now += altitude
            highest = max(now, highest)

        return highest