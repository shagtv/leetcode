from collections import deque
from functools import cache
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        result = root.val
        while q:
            new_q = deque()
            while q:
                node = q.popleft()
                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right)
            if new_q:
                result = new_q[0].val
                q = new_q
        return result
