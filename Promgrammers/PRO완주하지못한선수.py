#p = {"leo", "kiki", "eden"}
#c = {"eden", "kiki"}
from collections import Counter
import collections

p = ["mislav", "stanko", "mislav","mislav", "ana"]
c = ["stanko", "ana", "mislav", "mislav"]
#p = []
#c = []
def solution1(participant, completion): #Counter
    answer = Counter(participant) - Counter(completion)

    return list(answer.keys())[0]
    
print(solution1(p, c))


def solution2(participant, completion): #Zip

    participant.sort()
    completion.sort()

    for par, com in zip(participant, completion):
        print(par)
        print(com)
        if par != com:
            return par

    return participant[-1]

print(solution2(p, c))

def solution3(participant, completion): #Hash
    answer = Counter(participant) - Counter(completion)

    return list(answer.keys())[0]

#풀이법 zip, counter, hash
