import sys
from collections import deque
input = sys.stdin.readline
dx, dy = [-1,1,0,0], [0,0,-1,1] 

def find_swan(melt_map,visited, start, dest): #길이 있는지 없는지 확인
    N,M = len(melt_map), len(melt_map[0])
    next_start = deque()
    while start:
        x,y = start.popleft()
        for u in range(4):
            nx,ny = x+dx[u],y+dy[u]
            if (0 <= nx < N) and (0 <= ny < M) and not visited[nx][ny]:
                visited[nx][ny] = True
                if (nx,ny) == dest:
                    return True, None
                elif melt_map[nx][ny] == "X":
                    next_start.append((nx,ny))
                else: #그대로 건너뜀
                    start.append((nx,ny))
    return False, next_start

def melt_ice(map1,boundary): #각 경계점에서 bfs로 얼음이 녹는 시간 구함 #boundary 방금 막 .된 좌표 보관하는 queue
    N,M = len(map1),len(map1[0])
    queue = deque()
    while boundary:
        x,y,= boundary.popleft()
        for u in range(4):
            nx,ny = x+dx[u],y+dy[u]
            if (0 <= nx < N) and (0 <= ny < M):
                if map1[nx][ny] == "X": #녹이고 
                    map1[nx][ny] = "."
                    queue.append((nx,ny))
                #근처가 .이면 그냥 무시하면 된다(이미 녹은거니까)
    return queue

def solve():
    N,M = map(int,input().split())
    map1 = []
    swans, boundary = [], deque()
    for i in range(N):
        map1.append(list(input().rstrip()))
        for j in range(M):
            if map1[i][j] != "X":
                boundary.append((i,j))
            if map1[i][j] == "L":
                swans.append((i,j))

    result = 0
    start,visited = deque([swans[0]]), [[False]*M for _ in range(N)]
    visited[swans[0][0]][swans[0][1]] = True
    while boundary:
        hasfind,next_start = find_swan(map1,visited, start, swans[1]) #마지막에 길 찾은 곳 포함
        if hasfind:
            break
        next_boundary = melt_ice(map1,boundary)   
        start = next_start
        boundary = next_boundary
        result += 1
    print(result)

        
if __name__=="__main__":
    solve()