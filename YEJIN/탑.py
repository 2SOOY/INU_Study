def solution(heights):
    answer = []
    for i in range(len(heights)-1, 0, -1):
        print(i)
        flag = False
        send = heights[i]
        print(send)
        for j in range(i-1,-1,-1):
            print('j',j)
            if send < heights[j]:
                answer.append(j+1)
                flag = True
                break
        if not flag:
            answer.append(0)

    answer.append(0)
    print(answer)
    return answer[::-1]



if __name__ == '__main__':
    solution([6,9,5,7,4])