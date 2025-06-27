import sys
input = sys.stdin.readline

def bfs(original, x, y):
    max_len = 1
    q = set([(x, y, original[x][y])])  # set로 변경
    while q:
        x, y, alpha = q.pop()  # pop으로 변경
        max_len = max(max_len, len(alpha))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < c and 0 <= ny < r and original[nx][ny] not in alpha:
                q.add((nx, ny, alpha + original[nx][ny]))  # add로 변경
    return max_len

c,r = map(int, input().split())
original = []
for _ in range(c):
    original.append(list(input().strip()))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

print(bfs(original, 0, 0))