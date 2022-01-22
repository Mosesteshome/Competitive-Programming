import math
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        result= []
        answer =[]
        for x in range(len(points)):
            distance= ((points[x][0])*(points[x][0]))+ ((points[x][1])*(points[x][1]))
            y= (distance,points[x])
            result.append(y)
        result.sort()
        for x in range(k):
            answer.append(result[x][1])
        return answer
        
        
