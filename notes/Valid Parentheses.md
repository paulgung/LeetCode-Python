## Valid Parentheses

The stack data structure can come in handy here in representing this recursive structure of the problem. We can't really process this from the inside out because we don't have an idea about the overall structure. But, the stack can help us process this recursively i.e. from outside to inwards.

```python
# Dictionary and Stack
# Time complexity: O(n)  Space complexity O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {')':'(','}':'{',']':'['}
        for i in range(len(s)):
            stack.append(s[i])
            if(s[i] in dict.keys()) and stack[len(stack)-2] == dict[s[i]]:
                stack.pop()
                stack.pop()
        if stack == []:
            return True
        else:
            return False

res = Solution().isValid('(){}[]')
print(res)
```