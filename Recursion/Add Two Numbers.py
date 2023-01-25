#https://leetcode.com/problems/add-two-numbers/
# Definition for singly-linked list.
# class ListNode:
#     def init(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ans = ListNode()
        temp = 0
        while l1 or l2:
            if l1 and l2:
                sumi = l1.val + l2.val + temp
                if sumi > 9:
                    res.next = ListNode(val=sumi % 10)
                    temp = 1
                else:
                    res.next = ListNode(val=sumi)
                    temp = 0
                res = res.next 
                l1 = l1.next
                l2 = l2.next
            elif l1 == None:
                sumi = l2.val + temp
                if sumi > 9:
                    res.next = ListNode(val=sumi % 10)
                    temp = 1
                else:
                    res.next = ListNode(val=sumi)
                    temp = 0
                res = res.next
                l2 = l2.next
            elif l2 == None:
                sumi = l1.val + temp
                if sumi > 9:
                    res.next = ListNode(val=sumi % 10)
                    temp = 1
                else:
                    res.next = ListNode(val=sumi)
                    temp = 0
                res = res.next
                l1 = l1.next
        if temp == 1:
            res.next = ListNode(val= 1)
        return ans.next
