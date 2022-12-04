#
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        stack = []
        for x in range(len(nums1)):
            item = nums2.index(nums1[x])
            check = 0
            if (item != (len(nums2) -1)):
                while ( item != len(nums2)-1):
                    if(nums1[x] < nums2[item+1]):
                        stack.append(nums2[item + 1])
                        check = 1
                        break 
                    item += 1
            if (check == 0):
                    stack.append(-1)
        return(stack)