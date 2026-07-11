class Solution:
    def sumNumbers(self, root):
        
        def dfs(node, current):
            if not node:
                return 0

            # Build the number
            current = current * 10 + node.val

            # If it is a leaf node, return the number
            if not node.left and not node.right:
                return current

            # Continue searching left and right
            return dfs(node.left, current) + dfs(node.right, current)

        return dfs(root, 0)