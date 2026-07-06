class Solution:
    def pathSum(self, root, targetSum):
        result = []

        def dfs(node, remaining, path):
            if not node:
                return

            path.append(node.val)
            remaining -= node.val

            # If it's a leaf and sum matches
            if not node.left and not node.right:
                if remaining == 0:
                    result.append(path[:])
            else:
                dfs(node.left, remaining, path)
                dfs(node.right, remaining, path)

            # Backtrack
            path.pop()

        dfs(root, targetSum, [])
        return result