#https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true
def swap_case(s):
    ans = ""
    for x in s:
        if (x == x.lower()):
            ans += x.upper()
        elif (x == x.upper()):
            ans += x.lower()
    return ans


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)