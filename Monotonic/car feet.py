#https://leetcode.com/problems/car-fleet/
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = []
        res = 0
        cur = 0
        mapping = []
        for i in range(len(position)):
            mapping.append([position[i],speed[i]])
        mapping.sort()
        for i in mapping:
            time.append((target-i[0])/i[1])
        for x in time[::-1]:
            if x > cur:
                res +=1 
                cur = x
        return res