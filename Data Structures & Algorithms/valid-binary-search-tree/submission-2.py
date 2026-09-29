# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        # (node, left boundary, right boundary)
        queue = deque([(root, float('-inf'), float('inf'))])

        while queue:
            node, left_boundary, right_boundary = queue.popleft()
            if not (left_boundary < node.val < right_boundary):
                return False
            if node.left:
                queue.append((node.left, left_boundary, node.val))
            if node.right:
                queue.append((node.right, node.val, right_boundary))

        return True