## Generate Parentheses

#### Approach: Backtracking

**Intuition and Algorithm**

Instead of adding `'('` or `')'` every time , let's only add them when we know it will remain a valid sequence. We can do this by keeping track of the number of opening and closing brackets we have placed so far.

We can start an opening bracket if we still have one (of `n`) left to place. And we can start a closing bracket if it would not exceed the number of opening brackets.

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
      
        stack = []
        res = []
        
        def backtrack(openNum, closeNum):
            if (openNum == closeNum == n):
                res.append("".join(stack))
                return
            if (openNum < n):
                stack.append("(")
                backtrack(openNum + 1, closeNum)
                stack.pop()
            if (closeNum < openNum):
                stack.append(")")
                backtrack(openNum, closeNum + 1)
                stack.pop()

        backtrack(0, 0)
        return res

```



**Complexity Analysis**

Our complexity analysis rests on understanding how many elements there are in `generateParenthesis(n)`. This analysis is outside the scope of this article, but it turns out this is the `n`-th Catalan number.

- Time Complexity : O(4^n/√n). Each valid sequence has at most `n` steps during the backtracking procedure.
- Space Complexity : O(4^n/√n), as described above, and using O(n)*O*(*n*) space to store the sequence.

