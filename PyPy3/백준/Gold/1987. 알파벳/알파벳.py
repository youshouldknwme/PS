import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph= [[*map(str,input().strip())] for _ in range(n)]

dx,dy = [-1,0,1,0], [0,-1,0,1]
result = 0
def dfs(visited,count,x,y):
    global result
    result = max(result,count)
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if (0 <= nx < n) and (0 <= ny < m):
            a = graph[nx][ny]
            if a not in visited:
                visited.add(a)
                dfs(visited,count+1,nx,ny)
                visited.remove(a)

dfs(set(graph[0][0]),1,0,0)
print(result)