import math
#p = [95,90,99,99,80,99]
#s = [1, 1, 1, 1, 1, 1]
p = [99, 1]
s = [1, 99]
#p = [93,30,55]
#s = [1,30,5]

def solution(progresses, speeds):
    answer = []

    popList = []
    for p in range(0, len(progresses)):
        temp = math.ceil((100-progresses[p])/s[p])
        popList.append(temp)
    
    popList.reverse()

    while(len(popList) > 0):
        temp = popList.pop()
        sum = 1
        for i in range(len(popList)-1, -1, -1):
            if temp >= popList[i]:
                sum+=1
                popList.pop()
            else:
                break
        
        answer.append(sum)

    return answer

print(solution(p,s))