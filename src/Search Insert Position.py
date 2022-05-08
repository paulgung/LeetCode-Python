# Binary Search -- Lterative Method
# Time complexity:O(log n)  Space complexity:O(1)
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high + 1) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return low


# Binary Search -- Recusive Method
# Time complexity:O(log n)  Space complexity:O(1)
class Solution:
    def searchInsert(self, nums, target):
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


res = Solution().searchInsert([1, 3, 5, 6], 2)
print(res)
