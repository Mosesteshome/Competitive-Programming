#https://leetcode.com/problems/lru-cache/
class LRUCache:

    def __init__(self, capacity: int):
        self.dicti = {}
        self.size = 0
        self.capacity = capacity
 
    def get(self, key: int) -> int:
        if key in self.dicti:
            temp = self.dicti.pop(key)
            self.dicti[key] = temp
            return self.dicti[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.get(key)  == -1:
            if self.size == self.capacity:
                for x in self.dicti:
                    temp = x
                    break
                self.dicti.pop(temp)
                self.dicti[key] = value
            else:
                self.dicti[key] = value
                self.size += 1
        else:
            self.dicti[key] = value
 
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
