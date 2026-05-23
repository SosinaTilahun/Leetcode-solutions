# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head, left, right):
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head

        # Step 1: reach node before 'left'
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next

        # Step 2: reverse sublist
        current = prev.next
        nxt = None

        for _ in range(right - left):
            temp = current.next
            current.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next