import sys
from collections import deque

input = sys.stdin.readline

def D(num):
    return (num*2)%10000
def S(num):
    return (num+9999)%10000
def L(num):
    return num//1000+num%1000*10
def R(num):
    return num//10+num%10*1000

def find(start,end):
    com = [D,S,L,R]
    letter = ['D','S','L','R']
    visited = [-1]*10000 #해당 숫자가 될 때 사용한 문자와 그 전 숫자 기록
    visited[start] = start
    def bfs():
        routes = deque([start])
        while routes:
            x = routes.popleft()
            for i in range(4):
                nx = com[i](x)
                if nx == end:
                    visited[nx] = (x,letter[i])
                    return 
                if visited[nx] == -1:
                    routes.append(nx)
                    visited[nx] = (x,letter[i])
    def backtracking(visited,end):
        target = end
        st = ''
        while visited[target] != target:
            target, s = visited[target]
            st = st+s
        return st[::-1]
    bfs()
    return backtracking(visited,end)

for _ in range(int(input())):
    reg, target = map(int,input().split())
    print(find(reg,target))