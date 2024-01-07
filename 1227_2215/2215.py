class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res = []
        list1, list2 = set(nums1), set(nums2)

        res.append(list(list1 - list2))
        res.append(list(list2 - list1))

        return res