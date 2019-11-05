def solution(arrangement):
    stack = []
    cnt = 0
    for i in range(len(arrangement)):
        if arrangement[i] == '(':
            stack.append('(')
        else:
            stack.pop()
            if arrangement[i-1] == ')': # 연속으로 ))이 나온 경우 그냥 +1
                cnt += 1
            else:
                cnt += len(stack)
    return cnt




if __name__ == '__main__':
    solution('()(((()())(())()))(())')