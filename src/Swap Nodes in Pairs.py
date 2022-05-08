# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Approach: Recursion
# Time complexity : O(n)
# Space complexity : O(1)
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, curr = dummy, head
        while curr and curr.next:
            # save third and second nodes
            third = curr.next.next
            second = curr.next

            # reverse the nodes
            second.next = curr
            curr.next = third
            prev.next = second

            # update the nodes
            prev = curr
            curr = third
        return dummy.next
