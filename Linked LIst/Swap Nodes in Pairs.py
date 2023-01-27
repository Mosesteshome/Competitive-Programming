#https://leetcode.com/problems/swap-nodes-in-pairs/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d=ListNode(0,head)
        prev=d
        curr=head
        while curr and curr.next:
            prev.next = curr.next
            curr.next = curr.next.next
            prev.next.next = curr
            curr = curr.next
            prev = prev.next.next
        return d.next
        
    
