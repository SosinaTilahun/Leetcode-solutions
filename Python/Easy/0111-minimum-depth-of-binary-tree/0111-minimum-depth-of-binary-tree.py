class Solution:
    def minDepth(self, root):

        # If tree is empty
        if root is None:
            return 0

        # If node is a leaf
        if root.left is None and root.right is None:
            return 1

        # If left child does not exist
        if root.left is None:
            return 1 + self.minDepth(root.right)

        # If right child does not exist
        if root.right is None:
            return 1 + self.minDepth(root.left)

        # If both children exist
        return 1 + min(self.minDepth(root.left),
                       self.minDepth(root.right))