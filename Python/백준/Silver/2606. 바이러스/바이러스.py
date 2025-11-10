import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
m = int(input())
vertex = [[] for _ in range(n)]
for _ in range(m):
    a,b = map(int, input().split())
    vertex[a-1].append(b-1)
    vertex[b-1].append(a-1)


visited = [False for _ in range(n)]
virus = -1
bfs = deque([0])
while bfs:
    x = bfs.popleft()
    if not visited[x]:
        bfs.extend(vertex[x])
        virus += 1
        visited[x] = True
        
print(virus)
