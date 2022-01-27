class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack =[]
        pair={')':'(','}':'{', ']':'['}
        for x in s:
            if x in pair:
                if stack and stack[-1] == pair[x]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(x)
        return True if not stack else False
