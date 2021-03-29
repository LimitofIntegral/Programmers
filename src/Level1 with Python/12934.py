import math as m
def solution(n):
    if m.sqrt(n) % 1 == 0:
        return (m.sqrt(n) + 1) * (m.sqrt(n) + 1)
    else:
        return -1