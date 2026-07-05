class Solution:
    def sortedListToBST(self, head):
        
        if not head:
            return None
        
        if not head.next:
            return TreeNode(head.val)

        # Find middle
        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # slow is middle
        root = TreeNode(slow.val)

        # break list
        if prev:
            prev.next = None

        # left half
        root.left = self.sortedListToBST(head if slow != head else None)

        # right half
        root.right = self.sortedListToBST(slow.next)

        return root