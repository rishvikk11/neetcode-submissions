# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue_p = deque([p])
        queue_q = deque([q])

        while queue_p and queue_q:
            # level order traversal
            for _ in range(len(queue_p)):
                node_p = queue_p.popleft()
                node_q = queue_q.popleft()
                if not node_p and not node_q:
                    continue
                if (not node_p and node_q) or (node_p and not node_q):
                    return False
                if node_p.val != node_q.val:
                    return False

                queue_p.append(node_p.left)
                queue_p.append(node_p.right)
                queue_q.append(node_q.left)
                queue_q.append(node_q.right)

        return True