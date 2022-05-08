## Swap Nodes in Pairs

We need to use dummy head and two pointers: previous and current pointers. The idea is to change next pointers and meanwile store the current.next.next and current.next nodes in order to swap the two nodes.

```python
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
        prev, current = dummy, head
        while current and current.next:
            # save third and second nodes
            second = current.next
            third = current.next.next

            # reverse the nodes
            second.next = current
            current.next = third
            prev.next = second

            # update the nodes
            prev = current
            current = second
        return dummy.next

```