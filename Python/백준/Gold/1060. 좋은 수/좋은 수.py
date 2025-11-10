import sys
import heapq

def cal(start,end,num):
    return (num-start)*(end-num)-1 if (num-start)*(end-num)-1>0 else 0

input =sys.stdin.readline
L = int(input())
S = [0]+[*map(int,input().split())]
S.sort()
n = int(input())
h = []
for i in range(L):
    a,b = S[i],S[i+1]
    w = (n+1)//2
    if b-a <= n: #(a,b) 구간 사이의 모든 수를 후보군에 넣어야함
        for s in range(a+1,b+1):
            heapq.heappush(h,(cal(a,b,s),s))
    else: #최대 w개 까지만\
        for s in range(a+1,a+w+1):
            heapq.heappush(h,(cal(a,b,s),s))
        for s in range(b-w+1,b+1):
            heapq.heappush(h,(cal(a,b,s),s))
if len(h) < n: #heap에 후보군을 더 넣어야 함
    for s in range(S[-1]+1,S[-1]+1+n-len(h)):
        heapq.heappush(h,(float("inf"),s))
for _ in range(n):
    print(heapq.heappop(h)[1],end=" ")