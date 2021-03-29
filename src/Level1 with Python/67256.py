def d(a, b):
    temp1 = a[0] - b[0]
    temp2 = a[1] - b[1]
    if temp1 < 0:
        temp1 = -temp1
    if temp2 < 0:
        temp2 = -temp2
    return temp1 + temp2

def solution(numbers, hand):
    field = [(1, 0), (0, 3), (1, 3), (2, 3), (0, 2), (1, 2), (2, 2), (0, 1), (1, 1), (2, 1)]
    L = [0, 0]
    R = [2, 0]
    answer = ''
    for i in numbers:
        if i in [1, 4, 7]:
            answer += 'L'
            L = field[i]
        elif i in [3, 6, 9]:
            answer += 'R'
            R = field[i]
        else:
            if d(L, field[i]) > d(R, field[i]):
                answer += 'R'
                R = field[i]
            elif d(L, field[i]) < d(R, field[i]):
                answer += 'L'
                L = field[i]
            else:
                if hand == 'right':
                    answer += 'R'
                    R = field[i]
                else:
                    answer += 'L'
                    L = field[i]
    return answer