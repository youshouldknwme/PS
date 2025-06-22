import sys
input = sys.stdin.readline

n = int(input())
max_dp,min_dp = [0]*3,[0]*3
dps,funs = [max_dp,min_dp], [max,min]
for i in range(n):
    score = [*map(int,input().split())]
    for dp,f in zip(dps,funs):
        if i == 0:
            dp[0],dp[1],dp[2] = score[0],score[1],score[2]
        else:
            temp = dp[1]
            dp[1] = f(dp)+score[1]
            dp[0] = f(dp[0],temp)+score[0]
            dp[2] = f(temp,dp[2])+score[2]
print(max(max_dp),min(min_dp))