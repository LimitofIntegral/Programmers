def solution(s):
    N = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    if len(s) == (4 or 6):
        for i in s:
            if i not in N:
                return False
        return True
    else:
        return False