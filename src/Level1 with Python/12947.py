def solution(x):
    return False if x % sum(list(map(int, [i for i in str(x)]))) else True