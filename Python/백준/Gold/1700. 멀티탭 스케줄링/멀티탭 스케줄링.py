import sys
import heapq
input = sys.stdin.readline

n,k = map(int,input().split())
appears = [[] for _ in range(k+1)]

order = [*map(int,input().split())]
for i,x in zip(range(k),order):
    heapq.heappush(appears[x],i)

plugs = set()
total = 0
for i,x in zip(range(k),order):
    if x in plugs or len(plugs)<n:
        plugs.add(x)
        continue
    max_i = 0
    for x_dot in plugs:
        while True:
            if not appears[x_dot]:
                max = k
                break
            elif appears[x_dot][0] > i:
                max = appears[x_dot][0]
                break
            heapq.heappop(appears[x_dot])
        if max >= max_i:
            max_i = max
            target = x_dot
    plugs.remove(target)
    plugs.add(x)
    total += 1
print(total)