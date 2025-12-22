import sys
from collections import deque
input = sys.stdin.readline
dx, dy = [-1,1,0,0], [0,0,-1,1] 

def find_cluster(mat,x,y): #(x,y)에서 시작한 cluster가 공중에 떠 있는가?
    R,C = len(mat),len(mat[0])
    visited,issperated = [[False]*C for _ in range(R)], True
    elements= [] #floor 지만 matrix 구조상 max임
    bfs = deque([(x,y)])
    visited[x][y] = True
    while bfs:
        x,y = bfs.popleft()
        elements.append((x,y))
        if x == R-1:
            issperated = False
        for u in range(4):
            nx,ny = x+dx[u],y+dy[u]
            if (0<= nx < R) and (0 <= ny <C):
                if (mat[nx][ny] == "x") and (not visited[nx][ny]):
                    bfs.append((nx,ny))
                    visited[nx][ny] = True
    return issperated, elements



def down_cluster(mat,elements): #cluster를 중력으로 내리기(꼭 floor로 인해 down이 끝나는 건 아니다)
    R,C = len(mat), len(mat[0])
    mat_copy = [["."]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            mat_copy[i][j] = mat[i][j]
    elements.sort(reverse=True)
    for k in range(1,R):
        candown = True #한칸 더 down할 수 있는지 체크
        for (x,y) in elements:
            if x+k < R and mat_copy[x+k][y] == ".":
                mat_copy[x+k][y] = "x"
                mat_copy[x+k-1][y] = "."
            else:
                candown = False
        if not candown:
            break
    k -= 1
    for (x,y) in elements:
        mat[x+k][y] = "x"
        mat[x][y] = "."


def solve():
    R,C = map(int,input().split())
    mineral_map = [list(input().rstrip()) for _ in range(R)]
    N = int(input())
    throws = [*map(int,input().split())]
    for i in range(N):
        height = R - throws[i]
        if i%2 == 0: #왼쪽 -> 오른쪽
            for j in range(C):
                if mineral_map[height][j] == "x":
                    break
        else: #오른쪽 -> 왼쪽
            for j in range(C-1,-1,-1):
                if mineral_map[height][j] == "x":
                    break
        mineral_map[height][j] = "."
        for u in range(4):
            nx,ny = height+dx[u], j+dy[u]
            if (0<= nx < R) and (0 <= ny < C):
                if mineral_map[nx][ny] == "x":
                    isseperated,elements = find_cluster(mineral_map,nx,ny)
                    if isseperated:
                        down_cluster(mineral_map, elements)
    print("\n".join(["".join(arr) for arr in mineral_map]))      

        
if __name__=="__main__":
    solve()