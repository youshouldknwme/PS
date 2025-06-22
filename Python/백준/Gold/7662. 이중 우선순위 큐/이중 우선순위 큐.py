import sys
import heapq
from collections import deque

input = sys.stdin.readline

for _ in range(int(input())):
    k = int(input())
    max_h,min_h = [],[]
    deleted = [False]*k
    i = 0
    for _ in range(k):
        com,num = input().split()
        if com=="I":
            heapq.heappush(min_h,(int(num),i))
            heapq.heappush(max_h,(-int(num),i))
            i += 1
        elif com=="D":
            while num == '-1' and min_h:
                _, id = heapq.heappop(min_h)
                if not deleted[id]:
                    deleted[id] = True
                    break
            while num == '1' and max_h:
                _, id = heapq.heappop(max_h)
                if not deleted[id]:
                    deleted[id] = True 
                    break 
    while max_h:
        _,max_id = max_h[0]
        if deleted[max_id]:
            heapq.heappop(max_h)
        else:
            break          
    while min_h:
        _,min_id = min_h[0]
        if deleted[min_id]:
            heapq.heappop(min_h)
        else:
            break
    if max_h and min_h:
        print(-max_h[0][0], min_h[0][0])
    else:
        print("EMPTY")