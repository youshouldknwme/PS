import sys
from collections import deque

def init(graph, cabexists,n,m,k):
    for i in range(k):
        y,x = map(int, input().split())
        cabexists[x][y]= i
        if x-1 >= 0 and cabexists[x-1][y] >= 0:
            graph[i].append(cabexists[x-1][y])
            graph[cabexists[x-1][y]].append(i)
        if x+1 < m and cabexists[x+1][y] >= 0:
            graph[i].append(cabexists[x+1][y])
            graph[cabexists[x+1][y]].append(i)
        if y-1 >= 0 and cabexists[x][y-1] >= 0:
            graph[i].append(cabexists[x][y-1])
            graph[cabexists[x][y-1]].append(i)
        if y+1 < n and cabexists[x][y+1] >= 0:
            graph[i].append(cabexists[x][y+1])
            graph[cabexists[x][y+1]].append(i)


input = sys.stdin.readline
a = int(input())
for _ in range(a):
    n,m,k = map(int, input().split())
    cabexists = [[-1 for _ in range(n)] for _ in range(m)]
    graph = [[] for _ in range(k)]
    init(graph, cabexists,n,m,k)


    visited = [False for _ in range(k)]
    numbers = 0
    for i in range(k):
        if not visited[i]:
            bfs = deque([i])
            visited[i]= True
            while bfs:
                v = bfs.popleft()
                for l in graph[v]:
                    if not visited[l]:
                        bfs.append(l)
                        visited[l]=True
            numbers += 1
    print(numbers)