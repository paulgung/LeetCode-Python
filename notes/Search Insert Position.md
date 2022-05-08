## Search Insert Position

You must write an algorithm with `O(log n)` runtime complexity.

Let's use the binary search

There are two ways to create binary search: **Iterative** and **Recursive** Method.

```python
# Binary Search -- Lterative Method
# Time complexity:O(log n)  Space complexity:O(1)
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return low
```

```python
# Binary Search -- Recusive Method
# Time complexity:O(log n)  Space complexity:O(1)
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return 0
        N = len(nums)
        mid = N // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.searchInsert(nums[:mid], target)
        else:
            res = self.searchInsert(nums[mid + 1:], target)
            return res + mid + 1
```