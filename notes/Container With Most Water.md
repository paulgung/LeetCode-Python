## Container With Most Water

The aim is to maximize the area formed between the vertical lines. The area of any container is calculated using the shorter line as length and the distance between the lines as the width of the rectangle.

```
Area = length of shorter vertical line * distance between lines
```

We can definitely get the maximum width container as the outermost lines have the maximum distance between them. However, this container **might not be the maximum in size** as one of the vertical lines of this container could be really short.

Start with the maximum width container and go to a shorter width container if there is a vertical line longer than the current containers shorter line. This way we are compromising on the width but we are looking forward to a longer length container.

#### Approach 1: Brute Force

**Algorithm**

In this case, we will simply consider the area for every possible pair of the lines and find out the maximum area out of those.

```python
# Approach 1: Brute Force
# Time complexity : O(n^2) Calculating area for all  height pairs.
# Space complexity : O(1). Constant extra space is used.
class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        for i in range(len(height)):
            for j in range(i+1,len(height)):
                area = max(min(height[i],height[j])*(j-i),area)
        return area
```

**Complexity Analysis**

- Time complexity : O(n^2) Calculating area for all  height pairs.
- Space complexity : O(1). Constant extra space is used.

#### Approach 2: Two Pointer Approach

**Algorithm**

The intuition behind this approach is that the area formed between the lines will always be limited by the height of the shorter line. Further, the farther the lines, the more will be the area obtained.

We take two pointers, one at the beginning and one at the end of the array constituting the length of the lines. Futher, we maintain a variable text{maxarea} to store the maximum area obtained till now. At every step, we find out the area formed between them, update text{maxarea} and move the pointer pointing to the shorter line towards the other end by one step.

The algorithm can be better understood by looking at the example below:

```
1 8 6 2 5 4 8 3 7
```

- Time complexity : O(n). Single pass.
- Space complexity : O(1). Constant space is used.

```python
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
```