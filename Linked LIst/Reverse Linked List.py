#https://leetcode.com/problems/reverse-linked-list/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr =  head
        prev = frd = None
        while curr:
            frd = curr.next
            curr.next = prev
            prev = curr
            curr = frd
        return prev
