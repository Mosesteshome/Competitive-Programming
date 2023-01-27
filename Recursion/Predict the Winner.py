#https://leetcode.com/problems/predict-the-winner/description/
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:

        dicti = {}

        def turn(left,right,player):
            if left > right:
                return 0
            if (left,right,player) in dicti:
                return dicti[(left,right,player)]
            if player:
                dicti[(left,right,player)] = max(nums[left] + turn(left+1,right,not player),nums[right]+turn(left,right-1,not player))
            else:
                dicti[(left,right,player)] = min(-nums[left]+ turn(left+1,right,not player),-nums[right]+turn(left,right-1,not player))
            return dicti[(left,right,player)]
        
        return turn(0,len(nums)-1,True) >= 0

        
        
