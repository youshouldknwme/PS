import sys
input = sys.stdin.readline
out_lines = []

for _ in range(int(input())):
    N = int(input())
    y_scores = [0]*(N+1)
    for _ in range(N):
        x,y = map(int,input().split())
        y_scores[x]=y

    total = 0
    y_min = N+1
    for cand in range(1,N+1):
        if y_scores[cand] < y_min:
            y_min = y_scores[cand]
            total += 1
    out_lines.append(str(total))
sys.stdout.write("\n".join(out_lines))

#굳이 정렬 필요x