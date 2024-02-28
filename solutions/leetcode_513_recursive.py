from collections import deque
from functools import cache
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        max_level  = 0
        max_value = None

        def helper(node, level):
            if not node:
                return
            nonlocal max_level, max_value
            if max_level < level:
                max_level = level
                max_value = node.val
            helper(node.left, level + 1)
            helper(node.right, level + 1)

        helper(root, 1)
        return max_value
