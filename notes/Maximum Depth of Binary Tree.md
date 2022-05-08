## Maximum Depth of Binary Tree

To calculate the maximum depth we can use the Depth-First Search. We call a helper function recursively and return the maximum depth between left and right branches.

Time: **O(N)** - for DFS
Space: **O(N)** - for the recursive stack

```python
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive Method
# TimeComplexity:O(n) SpaceComplexity:O(1)
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.res = 1
        if (root == None):
            return 0

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
```