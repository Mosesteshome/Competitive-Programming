#https://leetcode.com/problems/top-k-frequent-elements/
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        count = Counter(nums).most_common(k)
        for x in count:
            res.append(x[0])
        return res