p = [1,2,3,2,3]

def solution(prices):
    answer = [0]*len(prices)

    for p in range(len(prices)-2, -1, -1):
        for pp in range(p, len(prices)):
            if p == pp: continue
            answer[p]+=1
            if prices[p] > prices[pp]:
                break
    return answer

print(solution(p))