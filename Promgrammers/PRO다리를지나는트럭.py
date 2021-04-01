import collections

b = 2#100
w = 10#100
t = [7,4,5,6]#[10,10,10,10,10,10,10,10,10,10]

def solution(bridge_length, weight, truck_weights):
    answer = 0

    #t = collections.deque(truck_weights)
    Q = collections.deque([0]*bridge_length)

    while Q:
        answer+=1
        Q.popleft()

        if t:
            if sum(Q) + truck_weights[0] <= weight:
                Q.append(truck_weights.pop(0))
            else:
                Q.append(0)
        
        print(Q)
    return answer

print(solution(b,w,t))