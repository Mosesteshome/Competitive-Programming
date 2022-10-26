#https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    temp = set(arr)
    temp.remove(max(temp))
    print(max(temp))
    