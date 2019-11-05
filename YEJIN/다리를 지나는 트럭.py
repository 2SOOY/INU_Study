from collections import deque
def solution(bridge_length, weight, truck_weights):
    if len(truck_weights) <= bridge_length and sum(truck_weights) <= weight:
        return bridge_length + len(truck_weights)
    time = 1
    bridge = deque([0]*bridge_length)
    next = truck_weights.pop(0)
    
    while True:
        n = bridge.popleft()
        if sum(bridge) + next <= weight:
            bridge.append(next)
            if truck_weights:
                next = truck_weights.pop(0)
            else:
                print(time + bridge_length)
                return time + bridge_length
        else:
            bridge.append(0)
        time += 1



if __name__ == '__main__':
    # solution(2,10,[7,4,5,6])
    # solution(1,1,[1])
    # solution(10000,100,[10])
    solution(100,100,[10,10,10,10,10,10,10,10,10,10])