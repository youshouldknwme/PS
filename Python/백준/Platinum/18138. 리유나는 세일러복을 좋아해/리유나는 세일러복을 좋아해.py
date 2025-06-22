import sys
input = sys.stdin.readline

def dfs(a,graph,matches,visited):
    for b in graph[a]:
        if visited[b]:
            continue
        visited[b] = True
        if matches[b] == -1 or dfs(matches[b],graph,matches,visited):
            matches[b] = a
            return 1
    return 0


n,m = map(int,input().split())
graph = [[] for _ in range(n)]
w = [int(input()) for _ in range(n)]
for i in range(m):
    b = int(input())
    for j in range(n):
        a = w[j]
        if (a/2 <= b <= 3*a/4) or (a <= b <= 5*a/4):
            graph[j].append(i)   #a는 길이 그대로, b는 몇번째인지 들어감

matches = [-1]*m
result = 0
for a in range(n):
    visited = [False]*m #각 시작 vertex를 matching 할때마다 visited 초기화 필요
    result += dfs(a,graph,matches,visited)
print(result)