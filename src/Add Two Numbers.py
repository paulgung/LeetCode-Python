# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Time complexity: O(max(m, n)) Space complexity:O(max(m, n))
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


# # Test Code
# test1 = ListNode(1)
# test_p = test1
# test_p.next = ListNode(3)
#
# test2 = ListNode(2)
# test_p2 = test2
# test_p2.next = ListNode(4)
#
# res = Solution().addTwoNumbers(test1,test2)
# print(res.val)
# print(res.next.val)