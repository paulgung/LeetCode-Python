# Approach: Bit manipulation
# TimeComplexity O(N) SpaceComplexity O(1)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res = i ^ res
        return res
