class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_nums = {num : idx for idx, num in enumerate(nums)}
        for idx, num in enumerate(nums):
            find_num = target - num
            if find_num in dict_nums and dict_nums[find_num] != idx:
                return [idx, dict_nums[find_num]]