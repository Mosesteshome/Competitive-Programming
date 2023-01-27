#https://leetcode.com/problems/merge-two-sorted-lists/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ans = ListNode()
        temp1 = list1
        temp2 = list2
        # print(res)
        # print(ans)
        while temp1 != None and temp2 != None:
            if temp1.val >= temp2.val:
                res.next = temp2
                res = temp2
                temp2 = temp2.next
            else:
                res.next = temp1
                res = temp1
                temp1 = temp1.next
        if temp1 or temp2:
            res.next = temp1 if temp1 else temp2
        return ans.next
