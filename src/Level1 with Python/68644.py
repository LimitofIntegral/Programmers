def solution(numbers):
    answer = []
    for i in range (len(numbers) - 1):
        for j in range (len(numbers) - 1 - i):
            temp = numbers[i] + numbers[j + 1 + i]
            if temp not in answer:
                answer.append(temp)
    answer.sort()
    return answer