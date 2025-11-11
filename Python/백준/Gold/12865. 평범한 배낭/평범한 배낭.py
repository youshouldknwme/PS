import sys
input = sys.stdin.readline

def solve():
    N, K = map(int,input().split())
    wv_list = [[*map(int,input().split())] for _ in range(N)]
    dp = [[0]*(K+1) for _ in range(N)]
    for i in range(N):
        for j in range(K+1):
            if i==0 and j >= wv_list[i][0]:
                dp[i][j] = wv_list[i][1]
            elif j < wv_list[i][0]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-wv_list[i][0]]+wv_list[i][1])
    print(dp[N-1][K])
    return
    
if __name__=="__main__":
    solve()