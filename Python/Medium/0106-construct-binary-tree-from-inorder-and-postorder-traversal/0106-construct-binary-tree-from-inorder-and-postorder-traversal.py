# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder, postorder):

        inorder_map = {}
        for i, val in enumerate(inorder):
            inorder_map[val] = i

        self.post_idx = len(postorder) - 1

        def helper(left, right):

            if left > right:
                return None

            # Root from postorder
            root_val = postorder[self.post_idx]
            self.post_idx -= 1

            root = TreeNode(root_val)

            # Find split point
            mid = inorder_map[root_val]

            # Build right first
            root.right = helper(mid + 1, right)
            root.left = helper(left, mid - 1)

            return root

        return helper(0, len(inorder) - 1)