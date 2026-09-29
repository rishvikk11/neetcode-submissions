# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        rootp, rootq = p, q
        queue = deque()
        queue.append(rootp)
        queue.append(rootq)

        while queue:
            node_p = queue.popleft()
            node_q = queue.popleft()
            if (not node_p and node_q) or (node_p and not node_q):
                return False
            if not node_p and not node_q:
                continue
            if node_p.val != node_q.val:
                return False

            queue.append(node_p.left)
            queue.append(node_q.left)
            queue.append(node_p.right)
            queue.append(node_q.right)

        return True