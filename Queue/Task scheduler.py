#https://leetcode.com/problems/task-scheduler/
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        res = []
        if (n == 0):
            return(len(tasks))
        for x in range(len(tasks)*n):
            counter = 0
            newcount = (count.most_common())
            for j in range(len(newcount)):
                if ( newcount[j][1] > 0 and counter < n+1 ):
                    res.append(newcount[j][0])
                    count[newcount[j][0]] -= 1
                    counter += 1
            check = (count.most_common())
            if ( check[0][1] == 0):
                   break
            if(counter < n+1 ):
                diff = n - counter +1
                res += [1] * diff            
        return(len(res))