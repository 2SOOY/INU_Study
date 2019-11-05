import math

def solution(progresses, speeds):
    stack = []
    # 작업 시간
    for i in range(len(progresses)):
        stack.append(math.ceil((100 - progresses[i])/speeds[i]))
    answer = []
    i = 0
    while i < len(stack):
        day = stack[i]
        cnt = 0
        for j in range(i, len(stack)):
            if stack[j] <= day:
                cnt += 1
                i += 1
            else:
                break
        answer.append(cnt)
    return answer

if __name__ == '__main__':
    solution([93,30,55], [1,30,5])