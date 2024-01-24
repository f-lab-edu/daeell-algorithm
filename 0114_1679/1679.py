class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        start, end = 0, len(nums) - 1
        res = 0

        while start < end:
            tmp = nums[start] + nums[end]
            if tmp == k:
                res += 1
                start += 1
                end -= 1
            elif tmp < k:
                start += 1
            else:
                end -= 1

        return res