import sys
from collections import deque

inStr = str(sys.stdin.readline().strip()).split(' ')

N, M, V = [int(i) for i in inStr]

graph = {}

for i in range(0,M):
    inStr = str(sys.stdin.readline().strip()).split(' ')
    n1,n2 = [int(j) for j in inStr]
    if n1 not in graph:
        graph[n1] = [n2]
    elif n2 not in graph[n1]:
        graph[n1].append(n2)

    if n2 not in graph:
        graph[n2] = [n1]
    elif n1 not in graph[n2]:
        graph[n2].append(n1)

def bfs(graph, start):
    visited = []
    queue = deque()
    queue.append(start)

    while queue:
        temp = queue.popleft()
        if temp not in visited:
            visited.append(temp)
            if temp in graph:
                temp = list(set(graph[temp]) - set(visited))
                temp.sort()
                queue += temp
    return " ".join(str(i) for i in visited)

def dfs(graph, start):
    visited = []
    stack = [start]
    
    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            if n in graph:
                temp = list(set(graph[n]) - set(visited))
                temp.sort(reverse=True)
                stack+= temp
    return " ".join(str(i) for i in visited)

sys.stdout.write("%s\n" %dfs(graph, V))
sys.stdout.write("%s" %bfs(graph, V))

