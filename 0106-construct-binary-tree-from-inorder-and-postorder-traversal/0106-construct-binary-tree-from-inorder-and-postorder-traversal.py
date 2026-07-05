class Solution:
    def buildTree(self, inorder, postorder):
        index = {v: i for i, v in enumerate(inorder)}
        postIndex = [len(postorder) - 1]

        def dfs(left, right):
            if left > right:
                return None

            rootVal = postorder[postIndex[0]]
            postIndex[0] -= 1

            root = TreeNode(rootVal)

            mid = index[rootVal]

            # Right first!
            root.right = dfs(mid + 1, right)
            root.left = dfs(left, mid - 1)

            return root

        return dfs(0, len(inorder) - 1)