#https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true
DataNS = []
DataS = []
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        DataNS += [[name, score]]
        DataS += [score]
    check = sorted(set(DataS))[1]

    for i, j in sorted(DataNS):
        if j == check:
            print(i)