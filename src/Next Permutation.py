class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        decreasing_num = -1
        swap_num = 0
        for i in range(len(nums) - 1, 0, -1):
            if (nums[i - 1] < nums[i]):
                decreasing_num = i - 1
                break
            else:
                continue
        # If we don't find the decreasing number
        if (decreasing_num == -1):
            nums.sort()
            return

        for j in range(len(nums) - 1, decreasing_num, -1):
            if (nums[j] > nums[decreasing_num]):
                swap_num = j
                break
            else:
                continue

        # swap
        nums[decreasing_num], nums[swap_num] = nums[swap_num], nums[decreasing_num]
        nums[decreasing_num + 1:] = sorted(nums[decreasing_num + 1:])



Solution().nextPermutation([1, 3, 2])
