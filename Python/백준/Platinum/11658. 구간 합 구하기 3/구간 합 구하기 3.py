import sys
input = sys.stdin.readline

def init(tree,n):
    for i in range(1,n+1): #각 row단위 bottom-up
        for j in range(1,n+1):
            j2 = j + (j & -j)
            if j2 <= n:
                tree[i-1][j2-1] += tree[i-1][j-1]
    
    for j in range(1,n+1): #각 column 단위 bottom up
        for i in range(1,n+1):
            i2 = i + (i & -i)
            if i2 <=  n:
                tree[i2-1][j-1] += tree[i-1][j-1]

def update(tree,n, x, y, value):
    i=x
    while i<=n:
        j=y
        while j<=n:
            tree[i-1][j-1]+=value 
            j += (j & -j)
        i += (i & -i)
    return None

def sum(tree,x,y):
    if x==0 or y==0:
        return 0
    i=x
    total=0
    while i>=1:
        j=y
        while j>=1:
            total += tree[i-1][j-1]
            j -= (j& -j)
        i -= (i&-i)
    return total

def prefixsum(tree,x1,y1,x2,y2):
    return sum(tree,x2,y2)-sum(tree,x1-1,y2)-sum(tree,x2,y1-1)+sum(tree,x1-1,y1-1)

n,m = map(int,input().split())
array = [[*map(int,input().split())] for _ in range(n)]
tree = [[array[i][j] for j in range(n)] for i in range(n)]
init(tree,n)

output_lines = []
for _ in range(m):
    p,*a = map(int,input().split())
    if p==0:
        i,j,num = a
        update(tree,n,i,j,num-array[i-1][j-1])
        array[i-1][j-1]=num
    elif p==1:
        x1,y1,x2,y2 = a
        result=prefixsum(tree,x1,y1,x2,y2)
        output_lines.append(str(result))


sys.stdout.write("\n".join(output_lines))