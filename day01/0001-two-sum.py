class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_nums = {num : idx for idx, num in enumerate(nums)}
        for idx, num in enumerate(nums):
            find_num = target - num
            if find_num in dict_nums and dict_nums[find_num] != idx:
                return [idx, dict_nums[find_num]]

# 정렬 + 이진탐색            
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_and_idx = [(num, idx)for idx, num in enumerate(nums)]
        num_and_idx.sort()
        for i in range(len(nums)):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if num_and_idx[mid][0] == target - num_and_idx[i][0]:
                    if mid != i: # 두 요소가 서로 다른 인덱스를 가질 때만 반환
                        return sorted([num_and_idx[i][1], num_and_idx[mid][1]])
                    else: # 같은 요소를 참조하는 경우, 이진 탐색 계속
                        if mid + 1 < len(nums) and num_and_idx[mid + 1][0] == target - num_and_idx[i][0]:
                            return sorted([num_and_idx[i][1], num_and_idx[mid + 1][1]])
                        elif mid - 1 >= 0 and num_and_idx[mid - 1][0] == target - num_and_idx[i][0]:
                            return sorted([num_and_idx[i][1], num_and_idx[mid - 1][1]])
                        break
                elif num_and_idx[mid][0] < target - num_and_idx[i][0]:
                    left = mid + 1
                else:
                    right = mid - 1
        return None