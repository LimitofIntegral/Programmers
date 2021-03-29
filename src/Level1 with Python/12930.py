def solution(s):
    arr = list(s.split(" "))
    answer = ''
    for i in range (len(arr)):
        for j in range (len(arr[i])):
            if j % 2 == 1:
                answer += arr[i][j].lower()
            else:
                answer += arr[i][j].upper()
        if i != (len(arr) - 1):
            answer += ' '
    return answer