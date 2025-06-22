import sys
input = sys.stdin.readline

M,N = map(int,input().split())
graph = [[*map(int,input().split())] for _ in range(M)]

cord1 = [(0,1),(1,0)]
cord2 = [(0,1),(-1,0)] 
tshapes = [[(-1,0),(1,0),(0,-1)],[(-1,0),(1,0),(0,1)],
           [(0,-1),(0,1),(1,0)],[(0,-1),(0,1),(-1,0)]]
def sol(x,y):
    def dfs(x,y,count,sum,cord):
        if count == 4:
            return sum
        d_max = 0
        for (dx,dy) in cord:
            nx, ny = x+dx,y+dy
            if (0<=nx<M) and (0<=ny<N):
                d_max = max(dfs(nx,ny,count+1,sum+graph[nx][ny],cord),d_max)
        return d_max
    
    def rarea(x,y): #정사각형 모양 처리
        if x+1<M and y+1<N:
            return graph[x][y]+graph[x+1][y]+graph[x][y+1]+graph[x+1][y+1]
        else:
            return 0

    def tarea(x,y): # ㅗ 모양 처리
        t_max = 0
        for tshape in tshapes:
            sum = graph[x][y] 
            for (dx,dy) in tshape:
                nx,ny = x+dx, y+dy
                if (0 <= nx < M) and (0<= ny < N):
                    sum += graph[nx][ny]
                else:
                    break
            t_max = max(sum,t_max)
        return t_max
    
    result = max(dfs(x,y,1,graph[x][y],cord1),dfs(x,y,1,graph[x][y],cord2))
    result = max(rarea(x,y),result)
    result = max(tarea(x,y),result)
    return result

result = 0
for i in range(M):
    for j in range(N):
        sol_max = sol(i,j)
        result = max(sol_max,result)
print(result)