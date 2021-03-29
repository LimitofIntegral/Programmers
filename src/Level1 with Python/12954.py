def solution(x, n):
    answer = []
    x_ = x
    for _ in range (n):
        answer.append(x_)
        x_ += x
    return answer