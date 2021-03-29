def solution(a, b):
    day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    temp = 4
    if a == 1:
        day_sum = b
    else:
        day_sum = sum(month[0 : a - 1]) + b
    temp += day_sum
    answer = day[temp % 7]
    return answer