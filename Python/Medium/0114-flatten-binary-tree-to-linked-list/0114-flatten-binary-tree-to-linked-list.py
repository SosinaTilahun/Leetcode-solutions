# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flatten(self, root):
        def dfs(node):
            if not node:
                return None

            # Flatten left and right subtrees
            left_tail = dfs(node.left)
            right_tail = dfs(node.right)

            # If there is a left subtree
            if node.left:
                # Attach original right subtree to end of left subtree
                left_tail.right = node.right

                # Move left subtree to the right
                node.right = node.left
                node.left = None

            # Return the tail of the flattened subtree
            return right_tail or left_tail or node

        dfs(root)