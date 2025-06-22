import sys
import heapq
from collections import defaultdict
from math import inf
input = sys.stdin.readline

def dijkstra(graph,current_distance,start,end):
    q = [(start,0)]
    while q:
        v, w = heapq.heappop(q)
        if w >= current_distance[v]:
            continue
        current_distance[v]= w
        for v_dot, w_dot in graph[v]:
            new_dist = w+w_dot
            if new_dist < current_distance[v_dot]:
                heapq.heappush(q,(v_dot,new_dist))
    return current_distance[end]

n = int(input())
m = int(input())
w_graph = defaultdict(list)
for i in range(m):
    a,b,w = map(int,input().split())
    w_graph[a].append((b,w))
current_distance = [inf]*(n+1)

start, end = map(int,input().split())
print(dijkstra(w_graph,current_distance,start,end))