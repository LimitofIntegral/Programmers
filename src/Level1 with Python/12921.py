import math as m

def solution(n):
    count = 0
    if n == 2 or n == 3:
        return 1
    else:
        for i in range (2, n + 1):
            plus = True
            for j in range (2, int(m.sqrt(i)) + 1):
                if i % j == 0:
                    plus = False
                    break
            if plus:
                count += 1
    return count