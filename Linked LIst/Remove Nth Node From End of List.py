#https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/884916718/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = fast = temp = ListNode(0,head)
        while n > 0  :
            fast= fast.next
            n -= 1
        while fast.next :
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return temp.next
