import math as m
def solution(a, b):
    g = m.gcd(a, b)
    return [g, a * b] if g == 1 else [g, a // g * b]