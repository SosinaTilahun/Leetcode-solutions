# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root, targetSum):
        result = []

        def dfs(node, remaining, path):
            if not node:
                return

            # Add current node to path
            path.append(node.val)

            # Check if it's a leaf and sum matches
            if not node.left and not node.right and remaining == node.val:
                result.append(path[:])   # copy path

            # Continue DFS
            dfs(node.left, remaining - node.val, path)
            dfs(node.right, remaining - node.val, path)

            # Backtrack
            path.pop()

        dfs(root, targetSum, [])
        return result