## 3Sum

We essentially need to find three numbers x, y, and z such that they add up to the given value. If we fix one of the numbers say x, we are left with the two-sum problem at hand!

The second train of thought for two-sum is, without changing the array, can we use additional space somehow? Like maybe a hash map to speed up the search?

```python
# Approach: Two pointer
# TimeComplexity: O(nlog(n)+O(n))  SpaceComplexity: O(1)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if (i > 0 and nums[i] == nums[i - 1]):
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if (nums[i] + nums[l] + nums[r] == 0):
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while (nums[l] == nums[l - 1] and l < r):
                        l += 1
                elif (nums[i] + nums[l] + nums[r] > 0):
                    r -= 1
                else:
                    l += 1
        return res

```