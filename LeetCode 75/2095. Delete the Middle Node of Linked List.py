
### Solution 1
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        count = 0
        curr = head
        while curr is not None:
            curr = curr.next
            count += 1

        i = 0
        prev = 0
        curr = head
        if head.next == None:
            return None
        else:
            while i <= (count // 2) - 1:
                if i == (count // 2) - 1:
                    curr.next = curr.next.next
                    break
                curr = curr.next
                i += 1
        return head

### Solution 2
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head.next is None:
            return None
        slow = fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            fast = fast.next.next
            slow = slow.next
        prev.next = prev.next.next
        return head


