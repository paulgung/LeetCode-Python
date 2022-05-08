# BruteForce O(n^2)
# Time Limit Exceeded
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if (prices[j] > prices[i]):
                    profit = max(profit, prices[j] - prices[i])
                else:
                    continue
        return profit


# Dynamic Programming
# TimeComplexity: O(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buyit = prices[0]
        for i in range(1, len(prices)):
            if (prices[i] < buyit):
                buyit = prices[i]
                continue
            else:
                profit = max(profit, prices[i] - buyit)
        return profit
