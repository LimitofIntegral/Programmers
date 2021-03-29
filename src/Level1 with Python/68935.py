def solution(n):
    N = n
    arr = []
    result = ''
    if N <= 2:
        return N
    else:
        count = 1
        while  3 ** count < N:
            count += 1

        if 3 ** count == N:
            pass
        else:
            count -= 1

        while count >= 0:
            a = 3 ** count
            b = N // a
            arr.append(str(b))
            N %= a
            count -= 1

    for i in range (len(arr)):
        result += arr[len(arr) - 1 - i]
    return int(result, 3)