from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        def is_poly(v):
            return sum(1 for i in v if i % 2) <= 1

        def helper(node, v):
            if not node:
                return 0
            v[node.val] += 1
            if not node.left and not node.right:
                result = 1 if is_poly(v) else 0
            else:
                result = helper(node.left, v) + helper(node.right, v)
            v[node.val] -= 1
            return result

        return helper(root, [0] * 10)


if __name__ == '__main__':
    given_root = TreeNode(2,
                          TreeNode(3,
                                   TreeNode(3), TreeNode(1)
                                   ),
                          TreeNode(1,
                                   None, TreeNode(1)
                                   )
                          )
    expected = 2

    solution = Solution()
    result = solution.pseudoPalindromicPaths(given_root)
    assert result == expected
