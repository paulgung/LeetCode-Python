# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        r = 0
        l = r - n
        slow = fast = head
        while (fast.next):
            r += 1
            l += 1
            fast = fast.next
        for i in range(l):
            slow = slow.next

        if (l==-1):
            head = head.next
        elif(l==0 and head.next.next == None):
            head.next = None
        else:
            slow.next = slow.next.next
        return head


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
