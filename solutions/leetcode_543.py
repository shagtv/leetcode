from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(node):
            if not node:
                return 0, 0
            l = height(node.left)
            r = height(node.right)
            return 1 + max(l[0], r[0]), max(l[1], r[1], l[0] + r[0])

        return height(root)[1]

