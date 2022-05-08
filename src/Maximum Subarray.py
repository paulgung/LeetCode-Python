# Approach 1: Sliding Window
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
