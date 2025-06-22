import sys
from bisect import bisect_left
input = sys.stdin.readline
n = int(input())
arr = [*map(int,input().split())]

target_arr = [arr[0]]
count = 1
for i in range(1,n):
    if arr[i] > target_arr[-1]:
        target_arr.append(arr[i])
        count += 1
    else:
        i_dot = bisect_left(target_arr,arr[i],lo=0)
        target_arr[i_dot] = arr[i]
print(count)