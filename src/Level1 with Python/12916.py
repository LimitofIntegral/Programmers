def solution(s):
    S = s.lower()

    if S.count('p') == S.count('y'):
        return True
    else:
        return False