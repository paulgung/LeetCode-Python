## Add Two numbers

#### Approach 1: Elementary Math

Keep track of the carry using a variable and simulate digits-by-digits sum starting from the head of list, which contains the least-significant digit.

**Complexity Analysis**

- Time complexity : O(max(m, n))  Assume that m and n represents the length of l1 and l2 respectively, the algorithm above iterates at most max(m, n)  times.
- Space complexity : O(max(m, n)).  The length of the new list is at most max(m,n) + 1.

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        :param l1: ListNode
        :param l2: ListNode
        :return: ListNode
        '''
        result = ListNode()
        dummyHead = result
        carry = 0
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            sum = val1 + val2 + carry
            carry = sum // 10
            out = sum % 10
            dummyHead.next = ListNode(out)
            dummyHead = dummyHead.next
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
        if carry :
            dummyHead.next = ListNode(carry)
        return result.next
```