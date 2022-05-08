# BackTracking
# TimeComplexity: O(4^n/√n) SpaceComplexity: O(4^n/√n)
class Solution:
    def generateParenthesis(self, n):
        # open parenthesis:"(" , close parenthesis: ")"
        # limit: open <= n and close <= open
        # stop when open == close == n

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


print(Solution().generateParenthesis(2))
