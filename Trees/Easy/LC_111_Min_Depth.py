# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def minDepth(self, root):
        if root is None:
            return 0

        # If left subtree is missing → we must go through right subtree
        if root.left is None:
            return 1 + self.minDepth(root.right)

        # If right subtree is missing → we must go through left subtree
        if root.right is None:
            return 1 + self.minDepth(root.left)

        # If both children exist → take the min depth of both
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
