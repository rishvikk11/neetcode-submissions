# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # the ancestor of two nodes is when p and q lie directly to the left and right of it or when one or the other is the ancestor itself
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if p.val < node.val and q.val < node.val:
                node = node.left
                queue.append(node)
            elif p.val > node.val and q.val > node.val:
                node = node.right
                queue.append(node)
            else:
                return node

