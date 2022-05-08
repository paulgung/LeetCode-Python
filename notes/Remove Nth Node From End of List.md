## Remove Nth Node From End of List

Maintain two pointers and update one with a delay of n steps.

Create two variables slow and fast, both pointing towards the head.

Move fast Pointer n steps ahead. Like, create a loop from 0 to n. if n == number of nodes then delete the head node.

Now take one step at a time, slow and fast, until you reach the end. Because it is ahead, the fast pointer will undoubtedly reach the end before the slow pointer. When the fast pointer reaches the end of the list, the slow pointer will be n steps behind it, or n steps behind the list’s end. When the fast pointer reaches the end of the list, the slow pointer will be n steps behind it, or n steps behind the list’s end.

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head
        # Move fast pointer n steps ahead
        for i in range(n):
            if fast.next is None:
                # If n is equal to the number of nodes, delete the head node
                head = head.next
                return head
            fast = fast.next

        while (fast.next):
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head
```