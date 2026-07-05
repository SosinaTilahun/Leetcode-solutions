class Solution:
    def buildTree(self, preorder, inorder):
        index = {v: i for i, v in enumerate(inorder)}
        preIndex = [0]   # use a list so it can be modified

        def dfs(left, right):
            if left > right:
                return None

            rootVal = preorder[preIndex[0]]
            preIndex[0] += 1

            root = TreeNode(rootVal)

            mid = index[rootVal]

            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)

            return root

        return dfs(0, len(inorder) - 1)