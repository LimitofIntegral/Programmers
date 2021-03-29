def solution(s):
    temp = []
    for i in s:
        temp += i
    temp.sort(reverse=True)
    result = ''
    for i in temp:
        result += i
    return result