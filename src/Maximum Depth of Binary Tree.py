# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive Method
# TimeComplexity:O(2^n) SpaceComplexity:O(1)
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if (root == None):
            return 0
        self.res = 1

        def backtrack(i, node):
            if (node.left == None and node.right == None):
                self.res = max(self.res, i)
                return
            if (node.left):
                backtrack(i + 1, node.left)
            if (node.right):
                backtrack(i + 1, node.right)

        backtrack(1, root)
        return self.res


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root, depth):
            if not root: return depth
            return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))

        return dfs(root, 0)
