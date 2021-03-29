def solve(number, n):
    temp = bin(number)[2:]
    if len(temp) == n:
        return list(temp)
    else:
        while len(temp) < n:
            temp = '0' + temp
        return list(temp)

def solution(n, arr1, arr2):
    temp1 = [[] for i in range (n)]
    temp2 = [[] for i in range (n)]
    answer = []
    for i in range (n):
        temp1[i] = solve(arr1[i], n)
        temp2[i] = solve(arr2[i], n)
    for x, y in zip(temp1, temp2):
        temp = ''
        for i, j in zip(x, y):
            if i == "1" or j == "1":
                temp += '#'
            else:
                temp += ' '
        answer.append(temp)
    return answer