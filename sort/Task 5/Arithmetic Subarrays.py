#https://leetcode.com/problems/arithmetic-subarrays/
class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """
        temp=[]
        boolean = []
        for j in range(len(r)):
            temp = []
            check = True
            for i in range(l[j],r[j]+1):
                temp.append(nums[i])
                   
            temp.sort()

            for k in range(len(temp)-1):
                if (temp[k+1] - temp[k] == temp[1] - temp[0]):
                                              
                    check =True
                else:
                                   
                    check = False
                    break
            boolean.append(check)

        return boolean
                
                    
            

