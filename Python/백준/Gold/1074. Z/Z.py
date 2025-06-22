import sys

def div(x,y,N):
    if N == 0:
        return 0
    return div(x%(2**(N-1)),y%(2**(N-1)),N-1) + (2**(N-1))**2* (((x//(2**(N-1)))<<1) | (y//(2**(N-1))))

input = sys.stdin.readline
N, r, c = map(int, input().split())
result = div(r,c,N)
print(result)