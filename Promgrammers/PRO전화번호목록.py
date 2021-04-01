#phone_book = ["119", "97674223", "1195524421"]
phone_book = ["123", "456", "789"]
#phone_book = ["12", "123", "1235", "567", "88"]


# 완탐 해야함.. BFS, DFS?
# substr
def solution():
    answer = True
    for p in phone_book:
        for pp in phone_book:
            if p == pp: continue

            if pp.find(p) == 0:
                if len(pp) > len(p):
                    if pp[0:len(p)] == p:
                        answer = False
                        return answer
                elif len(pp) <= len(p):
                    if p[0:len(pp)] == pp:
                        answer = False
                        return answer

    return answer


print(solution())