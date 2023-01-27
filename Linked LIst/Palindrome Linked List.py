#https://leetcode.com/problems/palindrome-linked-list/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = temp = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        right = slow
        prev = None
        while right:
            nxt = right.next
            right.next = prev
            prev = right
            right = nxt
        while prev:
            if prev.val != temp.val:
                return False
            prev = prev.next
            temp = temp.next
        return True

        

        
         
