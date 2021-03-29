def solution(s, n):
    S = s
    answer = ''
    for i in S:
        if ord(i) == 32:
            answer += ' '
        else:
            if ord(i) >= 65 and ord(i) <= 90:
                answer += chr(65 + (ord(i) - 65 + n) % 26)
            else:
                answer += chr(97 + (ord(i) - 97 + n) % 26)
    return answer