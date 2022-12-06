#https://leetcode.com/problems/spiral-matrix/description/
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        verticalstart = 0
        horizontalstart = 0
        verticalend = len(matrix) -1
        horizontalend = len(matrix[0]) -1 
        count = 0
        length = len(matrix)* len(matrix[0])
        while (count < len(matrix)* len(matrix[0])):
            for i in range(horizontalstart,horizontalend+1):  
                if count == length:
                    break
                ans.append(matrix[verticalstart][i])
                count += 1
            for i in range(verticalstart+1,verticalend+1):
                if count == length:
                    break
                ans.append(matrix[i][horizontalend])
                count += 1
            for i in range(horizontalend-1,horizontalstart-1,-1):
                if count == length:
                    break
                ans.append(matrix[verticalend][i])
                count += 1
            verticalstart += 1
            for i in range(verticalend-1,verticalstart-1,-1):
                if count == length:
                    break
                ans.append(matrix[i][horizontalstart])
                count += 1       
            horizontalstart +=1
            verticalend -= 1
            horizontalend -= 1
        
        return (ans)
    