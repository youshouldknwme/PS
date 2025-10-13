import sys
input = sys.stdin.readline
out_lines = []

import sys
input = sys.stdin.readline

N,new_score,P = map(int, input().split())
if N == 0:
    print(1)
    exit()
scores = [*map(int,input().split())]

if N==P and new_score <= scores[-1]:
    print(-1)
    exit()
for i in range(N):
    if new_score >= scores[i]:
        print(i+1)
        break
else:
    print(N+1)