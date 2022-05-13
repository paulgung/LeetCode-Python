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
                cash[(i, j)] = dfs(i, j + 2) or (firstMatch and dfs(i + 1, j))  # don't use the star or use the star
                return cash[(i, j)]
            if firstMatch:
                cash[(i, j)] = dfs(i + 1, j + 1)
                return cash[(i, j)]
            cash[(i,j)] = False
            return False

        return dfs(0, 0)
