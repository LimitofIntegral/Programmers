def solution(n):
    return int(''.join(list(reversed(sorted([i for i in str(n)])))))