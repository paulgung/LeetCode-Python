## Median of Two Sorted Arrays

If we merge the two sorted arrays, the time complexity will be O(n+m), so we need to find some clever way. The core concept of my solution is divide and conquer. I partition the two sorted arrays, and find the possible result index in both two arrays, just use the binary search and do not check the elements one by one.

How can we know whether we have find the correct left array? we should maintain the expression Bleft<=Aright and Aleft<=Bright in case that the right partition is always bigger than the left one.

```python
# Approach: Binary Search: Divide and Conquer
# Time complexity: O(log(m+n))  Space complexity: O(1)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2
        total = len(A) + len(B)
        half = total // 2
        if len(A) > len(B):
            A, B = B, A
        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2  # A
            j = half - i - 2  # B
            Aleft = A[i] if i >= 0 else float('-infinity')
            Aright = A[i + 1] if (i + 1) < len(A) else float('infinity')
            Bleft = B[j] if j >= 0 else float('-infinity')
            Bright = B[j + 1] if (j + 1) < len(B) else float('infinity')
            if Bleft <= Aright and Aleft <= Bright:
                # odd
                if total % 2 == 1:
                    return min(Aright, Bright)
                # even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Bleft > Aright:
                l = i + 1
            else:
                r = i - 1
```