# https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=true
def count_substring(string, sub_string):
    count = 0
    check = 0
    for i in range(0, len(string)):
        if (string[i] == sub_string[0]) and (len(string)-len(sub_string) >= i):
            for j in range(0, len(sub_string)):
                 
                if (string[j + i] == sub_string[j]):
                    check = 1
                else:
                    check = 0
                    break
            if check == 1:
                count += 1;
                
    return count 

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)