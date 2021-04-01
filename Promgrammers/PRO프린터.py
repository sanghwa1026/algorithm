p = [1,2,2]#[2,1,3,2]
l = 0#2

def solution(priorities, location):
    answer = 0

    # zip, index , priorities
    lt = []
    for i, v in enumerate(priorities):
        lt.append([i,v])
        #print(i, v)

    #lt = sorted(lt, key=lambda x: (-x[1], x[0]))
    #print(lt)
    
    idx = 0
    while lt:
        print(lt)
        temp = lt.pop(0)
        
        t = sorted(lt, key=lambda x: (-x[1]))
        
        if(len(t) > 0):
            if temp[1] >= t[0][1]:
                idx+=1
                if location == temp[0]:
                    return idx
            else:
                lt.append(temp)    
                
    return answer

print(solution(p,l))