import sys

input = sys.stdin.readline

def polynomial_modp(n,p):
    if n == 0:
        return 1
    result = 1
    for i in range(2,n+1):
        result = (result*i)%p
    return result

def power_modp(n,pow,p):
    base, result = n,1 
    while pow > 0:
        if pow%2 == 1:
            result = (result*base)%p
        base = (base*base)%p
        pow = pow//2
    return result


def solve():
    n,k = map(int,input().split())
    p = 1000000007
    conso = polynomial_modp(n,p)
    denom =  (polynomial_modp(k,p)*polynomial_modp(n-k,p))%p
    denom_inver = power_modp(denom,p-2,p)
    print((conso*denom_inver)%p)
    

        
if __name__=="__main__":
    solve()