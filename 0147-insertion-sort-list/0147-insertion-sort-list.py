class Solution:
    def insertionSortList(self, head):
        if not head or not head.next:
            return head

        # Dummy node before the sorted list
        dummy = ListNode(0)

        current = head

        while current:
            # Save the next node before changing current.next
            next_node = current.next

            # Find where current belongs
            prev = dummy

            while prev.next and prev.next.val < current.val:
                prev = prev.next

            # Insert current between prev and prev.next
            current.next = prev.next
            prev.next = current

            # Move to the next unsorted node
            current = next_node

        return dummy.next