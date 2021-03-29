def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if i == 0:
            if participant[i] != completion[i]:
                answer = participant[i]
                break
        elif i == len(completion) - 1:
            if participant[i] == completion[i]:
                answer = participant[i + 1]
                break

        if participant[i] == completion[i]:
            pass
        else:
            answer = participant[i]
            break
    return answer