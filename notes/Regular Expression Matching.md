## Regular Expression Matching

**Intuition**

As the problem has an **optimal substructure**, it is natural to cache intermediate results. We ask the question dp(i, j): does text[i:] and pattern[j:] match? We can describe our answer in terms of answers to questions involving smaller strings.

**Algorithm**

We proceed with the same recursion as recursion, except because calls will only ever be made to `match(text[i:], pattern[j:])`, we use dp(i, j) to handle those calls instead, saving us expensive string-building operations and allowing us to cache the intermediate results.

```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Top-down Memorization
        cash = {}

        def dfs(i, j):
            if ((i, j) in cash):
                return cash[(i, j)]

            # base case
            if (i >= len(s) and j >= len(p)):
                return True
            if (j >= len(p)):
                return False

            firstMatch = i < len(s) and (s[i] == p[j] or p[j] == ".")
            if ((j + 1) < len(p) and p[j + 1] == "*"):
                cash[(i, j)] = dfs(i, j + 2) or (firstMatch and dfs(i + 1, j))  # don't or use the star
                return cash[(i, j)]
            if firstMatch:
                cash[(i, j)] = dfs(i + 1, j + 1)
                return cash[(i, j)]
            cash[(i,j)] = False
            return False

        return dfs(0, 0)
```



- Time Complexity: Let T, P be the lengths of the text and the pattern respectively. The work for every call to `dp(i, j)` for i=0, ... ,T;  j=0, ... ,P is done once, and it is O(1) work. Hence, the time complexity is O(TP).
- Space Complexity: The only memory we use is the O(TP) boolean entries in our cache. Hence, the space complexity is O(TP).