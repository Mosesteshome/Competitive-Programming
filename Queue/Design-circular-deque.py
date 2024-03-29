#https://leetcode.com/problems/design-circular-deque/
class MyCircularDeque:

    def __init__(self, k: int):
        self.x = []
        self.n = k

    def insertFront(self, value: int) -> bool:
        if (len(self.x)<self.n):
            self.x.insert(0,value)
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if (len(self.x)<self.n):
            self.x.append(value)
            return True
        return False
    def deleteFront(self) -> bool:
        if (len(self.x)>0):
            self.x.remove(self.x[0])
            return True
        return False
    def deleteLast(self) -> bool:
        if (len(self.x)>0):
            self.x.pop()
            return True
        return False
    def getFront(self) -> int:
        if (len(self.x)>0):
            return self.x[0]
        return -1
    def getRear(self) -> int:
        if (len(self.x)>0):
            return self.x[-1]
        return -1
    def isEmpty(self) -> bool:
        if (len(self.x)==0):
            return True
        return False

    def isFull(self) -> bool:
        if (len(self.x)==self.n):
            return True
        return False