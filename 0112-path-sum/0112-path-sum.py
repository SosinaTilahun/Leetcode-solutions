class Solution:
    def hasPathSum(self, root, targetSum):
        if not root:
            return False

        # If this is a leaf
        if not root.left and not root.right:
            return root.val == targetSum

        targetSum -= root.val

        return (self.hasPathSum(root.left, targetSum) or
                self.hasPathSum(root.right, targetSum))