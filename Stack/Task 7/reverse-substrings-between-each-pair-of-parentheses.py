#https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/
class Solution:
    def reverseParentheses(self, s: str) -> str:
        res = []
        temp = []
        for x in range(len(s)):
            res.append(s[x])
            if s[x] == "(":
                temp.append(x) 
            elif s[x] == ")":
                count = (len(temp) -1) 
                last = len(res)-1
                res[(temp[count]):last] = reversed(res[(temp[count]):last])
                temp.pop()
                res[-1] = "0"
                res[-2] = "0"
        res = [i for i in res if i != "0"]
        return "".join(res) 