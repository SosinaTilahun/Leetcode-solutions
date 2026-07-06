class Solution:
    def flatten(self, root):
        if not root:
            return

        self.flatten(root.left)
        self.flatten(root.right)

        # Save original right subtree
        temp = root.right

        # Move left subtree to right
        root.right = root.left
        root.left = None

        # Go to end of new right chain
        curr = root
        while curr.right:
            curr = curr.right

        # Attach original right subtree
        curr.right = temp