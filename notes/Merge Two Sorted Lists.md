## Merge Two Sorted Lists

For simplicity, we create a dummy node to which we attach nodes from lists. We iterate over lists using two-pointers and build up a resulting list so that values are monotonically increased.

Time: **O(n)**
Space: **O(1)**

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Time complexity:O(n)  Space complexity:O(1)
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        dummyHead = result
        while list1 and list2:
            if list1.val < list2.val:
                dummyHead.next = ListNode(list1.val)
                list1 = list1.next
            else:
                dummyHead.next = ListNode(list2.val)
                list2 = list2.next
            dummyHead = dummyHead.next
        while list1:
            dummyHead.next = ListNode(list1.val)
            list1 = list1.next
            dummyHead = dummyHead.next
        while list2:
            dummyHead.next = ListNode(list2.val)
            list2 = list2.next
            dummyHead = dummyHead.next
        return result.next
```