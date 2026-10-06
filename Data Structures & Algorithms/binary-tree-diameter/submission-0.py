# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # iterative dfs solution, postorder traversal, start at root, check heights and diameters
        stack = [root]
        mapping = {None: (0,0)} # key = node, value = (height, diameter)

        while stack:
            node = stack[-1]
            if node.left and node.left not in mapping:
                stack.append(node.left)
            elif node.right and node.right not in mapping:
                stack.append(node.right)
            else:
                node = stack.pop()
                left_height, left_diameter = mapping[node.left]
                right_height, right_diameter = mapping[node.right]

                mapping[node] = (1 + max(left_height, right_height), max(left_height + right_height, left_diameter, right_diameter))

        return mapping[root][1]
