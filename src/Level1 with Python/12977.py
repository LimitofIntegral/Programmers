def solution(nums):
    answer = 0
    for i in range (len(nums) - 2):
        for j in range (len(nums) - 2 - i):
            for k in range (len(nums) - 2 - i - j):
                temp = nums[i] + nums[i + j + 1] + nums[i + j + k + 2]
                chk = True
                for l in range (2, int(temp ** (1/2)) + 1):
                    if temp % l == 0:
                        chk = False
                        break
                if chk:
                    answer += 1
    return answer