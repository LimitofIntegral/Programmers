def solution(arr1, arr2):
    result = []
    for x, y in zip(arr1, arr2):
        temp = []
        for i, j in zip(x, y):
            temp.append(i + j)
        result.append(temp)
    return result