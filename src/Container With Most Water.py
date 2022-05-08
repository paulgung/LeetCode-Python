# Approach 1: Brute Force
# Time complexity : O(n^2) Calculating area for all  height pairs.
# Space complexity : O(1). Constant extra space is used.
class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                area = max(min(height[i], height[j]) * (j - i), area)
        return area


# Approach 2: Two Pointer Approach
# Time complexity : O(n). Single pass.
# Space complexity : O(1). Constant space is used.
class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        l = 0
        r = len(height) - 1
        while l < r:
            area = max(min(height[l], height[r]) * (r - l), area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return area
