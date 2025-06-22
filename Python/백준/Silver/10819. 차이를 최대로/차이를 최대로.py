import sys
input = sys.stdin.readline

def sol(arr,n):
    results = []

    def cal(cand,n):
        total = 0
        for i in range(n-1):
            total += abs(arr[cand[i]]-arr[cand[i+1]])
        return total

    def backtracking(cand,depth):
        if depth == n:
            results.append(cal(cand,n))
            return
        for i in range(n):
            if i in cand:
                continue
            cand.append(i)
            backtracking(cand,depth+1)
            cand.pop()
    backtracking([],0)
    return max(results)
    
n = int(input())
arr = [*map(int,input().split())]
print(sol(arr,n))

