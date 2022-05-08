## Counting Bits

It is very easy to come up with a solution with a runtime of `O(n log n)`. We just use the method mod() to caculate every single num and count the number of 1's 

The smarter way is use the dynamic programming:

​	Divide the numbers in ranges like [2-3], [4-7], [8-15] and so on. And try to generate new range from previous.

```python
# Dynamic Programming
# TimeComplexity:O(n) SpaceComplexity:O(1)
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp
```

```python
# Tricky Method
# TimeComplexity:O(n) SpaceComplexity:O(1)
def countBits(self, n: int) -> List[int]:
    return [bin(i)[2:].count("1") for i in range(n+1)]
```