# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        current = head

        while current:
            # Detect duplicates
            if current.next and current.val == current.next.val:
                duplicate_val = current.val

                # Skip all nodes with duplicate_val
                while current and current.val == duplicate_val:
                    current = current.next

                prev.next = current
            else:
                prev = prev.next
                current = current.next

        return dummy.next