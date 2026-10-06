# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # recursive dfs solution, postorder traversal
        self.res = 0

        def dfs(node):
            # base case
            if not node:
                return 0
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            self.res = max(self.res, left_height + right_height) # getting max diameter

            return 1 + max(left_height, right_height) # return max height at current node

        dfs(root)
        return self.res