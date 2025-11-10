import sys

input = sys.stdin.readline

def solve():
    n = int(input())
    num_list = [str(input().rstrip()) for _ in range(n)]
    num_list.sort()
    for i in range(0,n-1):
        length = len(num_list[i])
        if num_list[i] == num_list[i+1][:length]:
            print("NO")
            return
    print("YES")
    return
    
if __name__=="__main__":
    for _ in range(int(input())):
        solve()