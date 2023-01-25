#https://leetcode.com/problems/reverse-nodes-in-k-group/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ans = ListNode()
        count = k
        prev = None
        check = head
        leng = 0
        while check:
            leng += 1
            check = check.next
        leng = leng//k
        check = head
        dummy = ans
        while leng > 0:
            prev = None
            while count >= 1:
                # print(prev)
                fwd = check.next
                check.next = prev
                prev = check
                check = fwd
                count -= 1
            dummy.next = prev
            for i in range(k):
                dummy = dummy.next
            # prev = check
            count = k
            leng -=1
        dummy.next = check
        return ans.next
