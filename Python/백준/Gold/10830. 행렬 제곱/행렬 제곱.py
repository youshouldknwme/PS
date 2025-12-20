import sys
input =sys.stdin.readline

def mat_operation(mat1,mat2,n):
    mat = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result = 0
            for k in range(n):
                result += (mat1[i][k]*mat2[k][j])%1000
            mat[i][j] = result%1000
    return mat

def solve():
    n,b = map(int,input().split())
    mat =[[*map(int,input().split())] for _ in range(n)]
   
    result = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                result[i][j] = 1
    base = mat
    while b > 0:
        if b%2 == 1:
            result = mat_operation(result,base,n)
        base = mat_operation(base,base,n)
        b = b//2
    print('\n'.join([' '.join(map(str,row)) for row in result]))

        
if __name__=="__main__":
    solve()