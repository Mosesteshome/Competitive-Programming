#https://leetcode.com/problems/next-greater-node-in-linked-list/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        ans = [0] * len(nums)
        decstack = []
        for i in range(len(nums)):
            while decstack and nums[decstack[-1]]  < nums[i]:
                    x = decstack.pop()
                    ans[x] = nums[i] 
            decstack.append(i)
        return ans
