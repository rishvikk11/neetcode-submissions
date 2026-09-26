# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        # left -> right -> root
        # root -> right -> left (reversed) = variant of preorder
        stack, res = [], []
        stack.append(root)

        while stack:
            node = stack.pop()
            res.append(node.val)

            # we want to access right node first
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        # reverse this preorder
        return res[::-1]
