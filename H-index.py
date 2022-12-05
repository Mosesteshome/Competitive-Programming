#https://leetcode.com/problems/h-index/
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        count = 0
        citations.sort(reverse = True)
        if len(citations) == 0:
            return 0
        for x in range(len(citations)):
            if citations[x] > x:
                count += 1
        return (count)