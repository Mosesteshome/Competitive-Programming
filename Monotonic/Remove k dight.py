#https://leetcode.com/problems/remove-k-digits/
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        ans = []
        stack = []
        x = 0
        while x < (len(num)):
            while( stack and num[stack[-1]] > num[x]):
                temp = stack.pop()
                num = num[0:x] + num[x+1:len(num)]
                ans.append(num[temp])
                if ( len(ans) == k):
                    break
            stack.append(x)
            if (len(ans)==k):
                break
            x += 1
        j = k - len(ans)
        if (j != 0):
            y = len(num) - j
            num = num[0:y]
        print(ans)
        return str(int(num))
    
    """
    
    """

        