class Solution:
    def minCostClimbingStairs(self, cost):
        dp = {}
        cost.append(0)
        n = len(cost)
        for i in range(n):
            if i < 2:
                dp[i] = cost[i]
                continue
            dp[i] = min(dp[i-1] + cost[i], dp[i-2] + cost[i])
        return list(dp.values())[-1]

#######                    
print(Solution().minCostClimbingStairs([10,15,20]))