# dp
class Solution:
    def fib(self, n):
        dp = {0:0, 1:1}
        for i in range(2,n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

# 递归
# class Solution:
#     def fib(self, n):
#         if n == 0:
#             return 0
#         if n == 1:
#             return 1
#         res =  self.fib(n - 1) + self.fib(n - 2)
#         return res

#######
print(Solution().fib(4))