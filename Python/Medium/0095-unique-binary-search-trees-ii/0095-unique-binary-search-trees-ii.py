# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """

        if n == 0:
            return []

        def build(start, end):

            if start > end:
                return [None]

            trees = []

            for root_val in range(start, end + 1):

                left_trees = build(start, root_val - 1)
                right_trees = build(root_val + 1, end)

                for left in left_trees:
                    for right in right_trees:

                        root = TreeNode(root_val)
                        root.left = left
                        root.right = right

                        trees.append(root)

            return trees

        return build(1, n)