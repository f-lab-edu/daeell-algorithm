class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrences = {}
        for num in arr:
            if num in occurrences:
                occurrences[num] += 1
            else:
                occurrences[num] = 1

        seen = set()

        for freq in occurrences.values():
            if freq in seen:
                return False
            seen.add(freq)

        return True