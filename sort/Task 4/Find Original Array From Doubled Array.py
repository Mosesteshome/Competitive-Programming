#https://leetcode.com/problems/find-original-array-from-doubled-array/submissions/
import itertools
class Solution(object):
    def findOriginalArray(self, changed):
        """
        :type changed: List[int]
        :rtype: List[int]
        """

        ans=[]
        if len(changed)%2 !=0:
            return ans
        else:
            changed.sort()
            
            count =  Counter(changed)
            for x in changed:
                if count[x] > 0 and count[2*x] > 0:              
                    if x != 0:
                        ans.append(x)
                        count[x] -= 1
                        count[2*x] -= 1                    
                    elif count[x] > 1:
                        ans.append(x)
                        count[x]-= 1
                        count[2*x] -= 1
        if float(len(changed))/2!=len(ans):
               ans =[]
        return ans
