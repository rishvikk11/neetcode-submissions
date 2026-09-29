# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([(root, 1)])
        max_height = 1

        while queue:
            node, height = queue.popleft()
            if not node:
                continue
            max_height = max(max_height, height)

            if node.left:
                queue.append((node.left, height+1))
            if node.right:
                queue.append((node.right, height+1))

        return max_height
