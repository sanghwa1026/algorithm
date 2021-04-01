import sys
from collections import deque

N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())

graph = {}

for i in range(0,M):
    inLine = sys.stdin.readline().strip().split(' ')
    n1, n2 = [int(j) for j in inLine]

    if n1 not in graph:
        graph[n1] = [n2]
    elif n2 not in graph[n1]:
        graph[n1].append(n2)

    if n2 not in graph:
        graph[n2] = [n1]
    elif n1 not in graph[n2]:
        graph[n2].append(n1)

#sys.stdout.write("%s\n"% graph)

ans = 0

def dfs(graph, v):
    visit = []
    qu = deque([v])
    global ans

    while len(qu):
        temp = qu.popleft()
        if temp not in visit:
            visit.append(temp)
            if temp in graph:
                temp = list(set(graph[temp]) - set(visit))
                #print(temp)
                temp.sort(reverse=True)
                qu+=temp
                ans+=1
    #return " ".join(str(i) for i in visit)
dfs(graph, 1)
sys.stdout.write("%d" %int(ans-1))
#sys.stdout.write("%s" %bfs(graph, 1) + "%s" %ans-1)