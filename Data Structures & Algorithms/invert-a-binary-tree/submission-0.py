# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curr = root
        queue = deque([curr])
        visited = set()

        while queue:
            node = queue.popleft()
            if not node:
                continue
            self.switch_roots(node)
            queue.append(node.left)
            queue.append(node.right)

        return root

    def switch_roots(self, root):
        temp = root.right
        root.right = root.left
        root.left = temp