## Next Permutation

#### Approach: Single Pass Approach

**Algorithm**

First, we observe that for any given sequence that is in descending order, no next larger permutation is possible. For example, no next permutation is possible for the following array:

```
[9, 5, 4, 3, 1]
```

We need to find the first pair of two successive numbers a[i] and a[i-1], from the right, which satisfy a[i] > a[i-1]. Now, no rearrangements to the right of a[i-1] can create a larger permutation since that subarray consists of numbers in descending order. Thus, we need to rearrange the numbers to the right of a[i-1] including itself.

Now, what kind of rearrangement will produce the next larger number? We want to create the permutation just larger than the current one. Therefore, we need to replace the number a[i-1] with the number which is just larger than itself among the numbers lying to its right section, say a[j].

We swap the numbers a[i-1] and a[j]. We now have the correct number at index i-1. But still the current permutation isn't the permutation that we are looking for. We need the smallest permutation that can be formed by using the numbers only to the right of a[i-1]. Therefore, we need to place those numbers in ascending order to get their smallest permutation.

But, recall that while scanning the numbers from the right, we simply kept decrementing the index until we found the pair a[i] and a[i-1] where, a[i] > a[i-1]. Thus, all numbers to the right of a[i-1] were already sorted in descending order. Furthermore, swapping a[i-1] and a[j] didn't change that order. Therefore, we simply need to reverse the numbers following a[i-1] to get the next smallest lexicographic permutation.

The following animation will make things clearer:

![31_Next_Permutation](./images/31_Next_Permutation.gif)

```python
# Time complexity : O(n) Space complexity : O(1)
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
```



**Complexity Analysis**

- Time complexity : O(n)  In worst case, only two scans of the whole array are needed.
- Space complexity : O(1) No extra space is used. In place replacements are done.