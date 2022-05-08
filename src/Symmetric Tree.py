# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recusive Method
# TimeComplexity: O(log(n)) SpaceComplexity:O(1)
class Solution:
    def mirror(self, l_node, r_node):
        if (l_node != None and r_node != None):
            if (l_node.val != r_node.val):
                return False
            if (l_node.left == None and l_node.right == None and r_node.left == None and r_node.right == None):
                return True
            return self.mirror(l_node.left, r_node.right) and self.mirror(l_node.right, r_node.left)
        else:
            if (l_node == r_node == None):
                return True

        def isSymmetric(self, root: Optional[TreeNode]) -> bool:
            return self.mirror(root.left, root.right)


class Solution:
    def mirror(self, l_node, r_node):
        if (l_node == r_node == None):
            return True
        elif (l_node != None and r_node != None):
            if (l_node.val != r_node.val):
                return False
            if (l_node.left == None and l_node.right == None and r_node.left == None and r_node.right == None):
                return True
            return self.mirror(l_node.left, r_node.right) and self.mirror(l_node.right, r_node.left)

        def isSymmetric(self, root: Optional[TreeNode]) -> bool:
            return self.mirror(root.left, root.right)
