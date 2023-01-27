#https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head
        ans = []
        while fast:
            slow = slow.next
            fast = fast.next.next
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        while prev:
            ans.append(prev.val+head.val)
            prev = prev.next
            head = head.next
        return max(ans)
