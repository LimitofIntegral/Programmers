def solution(d, budget):
    d_ = sorted(d)
    sum, cnt = 0, 0
    while True:
        sum += d_[cnt]
        if sum > budget:
            return cnt
        else:
            cnt += 1

        if cnt == len(d_):
            return cnt