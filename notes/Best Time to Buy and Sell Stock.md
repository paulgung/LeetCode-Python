## Best Time to Buy and Sell Stock

```python
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
```

The points of interest are the peaks and valleys in the given graph. We need to find the largest peak following the smallest valley. We can maintain two variables - minprice and maxprofit corresponding to the smallest valley and maximum profit (maximum difference between selling price and minprice) obtained so far respectively.

```python
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
```