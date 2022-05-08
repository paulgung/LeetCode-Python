## Maximum Subarray

#### Approach: Sliding Window

Because of the way this algorithm uses optimal substructures (the maximum subarray ending at each position is calculated in a simple way from a related but smaller and overlapping subproblem: the maximum subarray ending at the previous position) this algorithm can be viewed as a simple/trivial example of dynamic programming

The runtime complexity of Kadane's algorithm is O(n)

```python
# Approach: Sliding Window
# TimeComplexity O(n) SpaceComplexity O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currentSum = 0
        for i in nums:
            if currentSum < 0:
                currentSum = 0
            currentSum += i
            maxSum = max(maxSum, currentSum)
        return maxSum
```