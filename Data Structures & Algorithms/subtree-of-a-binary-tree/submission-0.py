# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # use bfs to traverse through paths and for every path we obtain, check if it's equal to the subroot
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if self.isSameTree(node, subRoot):
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return False

    def isSameTree(self, root1, root2):
        queue1, queue2 = deque([root1]), deque([root2])

        while queue1 and queue2:
            node1, node2 = queue1.popleft(), queue2.popleft()
            if not node1 and not node2:
                continue
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False

            queue1.append(node1.left)
            queue1.append(node1.right)
            queue2.append(node2.left)
            queue2.append(node2.right)

        return True


