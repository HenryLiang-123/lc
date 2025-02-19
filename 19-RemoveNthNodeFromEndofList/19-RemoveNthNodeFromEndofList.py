// Last updated: 2/18/2025, 11:43:04 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # get length
        length = 0
        first = head
        while first:
            length += 1
            first = first.next
        length -= n
        dummy = ListNode(None)
        dummy.next = head
        second = dummy
        while length > 0:
            length -= 1
            second = second.next
        
        second.next = second.next.next

        return dummy.next
