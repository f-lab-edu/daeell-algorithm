class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        tmp = sum(nums[:k])
        res = tmp
        for i in range(1, len(nums) - k + 1):
            tmp = tmp - nums[i - 1] + nums[i + k - 1]
            res = max(tmp, res)

        return res / k