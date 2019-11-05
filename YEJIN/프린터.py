def solution(priorities, location):
    answer = []
    # 인덱스와 중요도를 묶은 리스트
    priorities = list(zip(range(0,len(priorities)), priorities))
    while priorities:
        idx, num = priorities.pop(0)
        for i in range(len(priorities)):
            if num < priorities[i][1]: # 중요도가 높은 문서가 존재하면
                priorities.append((idx,num))
                break
        if i == len(priorities)-1: # 중요도가 높은 문서가 존재하지 않았다면
            answer.append(idx)
    answer.append(idx) # 마지막 문서가 들어가지 않는 에러 처리
    return answer.index(location)+1

if __name__ == '__main__':
    solution([2,1,3,2], 2)