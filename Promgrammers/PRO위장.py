
c = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]


def solution(clothes):
    answer = 1

    dic = {}

    for item,cate in clothes:
        if cate in dic:
            dic[cate]+=1
        else:
            dic[cate] = 1

    print(dic)

    for c in dic:
        answer*=(dic[c]+1)

    return answer-1


print(solution(c))