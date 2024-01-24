class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        length = len(cost)

        for i in range(2, length):
            cost[i] = min(cost[i - 1], cost[i - 2]) + cost[i]

        return min(cost[-1], cost[-2])
    
# new solution - Space Complexity O(1)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        length = len(cost)
        pre_1, pre_2 = 0, 0
        for i in range(2, length + 1):
            current_cost = min(pre_1 + cost[i - 1], pre_2 + cost[i - 2])
            pre_2, pre_1 = pre_1, current_cost

        return pre_1