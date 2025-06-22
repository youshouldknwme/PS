import sys
input = sys.stdin.readline

def next(seq): #다음 확인할 수열
    a = seq.pop()
    if a == 3:
        next(seq)
    else:
        seq.append(a+1)

def isgood(seq): #마지막 문자는 무조건 포함해서 확인
    n = len(seq)
    for length in range(1, n // 2 + 1):
        if seq[n-2*length:n-length] == seq[n-length:n]:
            return False
    return True

N = int(input())
seq = [1]
while (not isgood(seq)) or (len(seq) < N):
    if not isgood(seq):
        next(seq)
    elif len(seq) < N:
        seq.append(1)
print(int("".join(map(str,seq))))
