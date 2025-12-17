import sys
import heapq

input = sys.stdin.readline


def solve():
    N = int(input())
    lower_heap, higher_heap = [],[]
    heapq.heappush(higher_heap, 10001)
    heapq.heappush(lower_heap,10001) #여기엔 -n 붙여서 넣음
    mid = int(input())
    result = [mid]
    for i in range(1,N):
        x = int(input())
        if i%2 == 1: #i=1,3,5.... mid index not change
            if x <= mid:
                heapq.heappush(lower_heap,-x)
                heapq.heappush(higher_heap,mid)
                mid = -heapq.heappop(lower_heap)
            else:
                heapq.heappush(higher_heap,x)
        else: #mid index change
            if x <= mid:
                heapq.heappush(lower_heap,-x)
            else:
                heapq.heappush(higher_heap,x)
                heapq.heappush(lower_heap,-mid)
                mid = heapq.heappop(higher_heap)
        result.append(mid)
    print("\n".join(map(str,result)))
    

            
if __name__=="__main__":
    solve()
