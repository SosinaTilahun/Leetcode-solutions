# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):

        inorder_map = {}
        for i, val in enumerate(inorder):
            inorder_map[val] = i

        self.pre_idx = 0

        def helper(left, right):

            if left > right:
                return None

            # Root from preorder
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1

            root = TreeNode(root_val)

            # Split inorder
            mid = inorder_map[root_val]

            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)

            return root

        return helper(0, len(inorder) - 1)