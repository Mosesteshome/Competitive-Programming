#https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = head
        
        while ans and ans.next:
            if ans.val == ans.next.val:
                ans.next = ans.next.next
            else:
                ans = ans.next
        return head
