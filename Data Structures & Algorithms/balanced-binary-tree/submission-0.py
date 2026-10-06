# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # postorder traversal
        def dfs(node):
            if not node:
                return [True, 0]

            left_height = dfs(node.left)
            right_height = dfs(node.right)

            # check if left and right are balanced then check height difference
            balanced = left_height[0] and right_height[0] and abs(left_height[1] - right_height[1]) <= 1

            return [balanced, 1 + max(left_height[1], right_height[1])]
        
        res = dfs(root)
        return res[0]
