#include <string>
#include <vector>
#include <queue>

using namespace std;

int bfs(int n, int cut, vector<vector<int>> wires) {
    wires.erase(wires.begin()+cut);
    vector<bool> visited(n+1,false);
    queue<int> que;
    
    que.push(1);
    visited[1] = true;
    int count = 1;
    while (!que.empty()) {
        int x = que.front();
        que.pop();
        for (const auto& wire : wires) {
            if (x == wire[0] || x == wire[1]) {
                int x_dot = (x == wire[0]) ? wire[1] : wire[0];
                if (!visited[x_dot]) {
                    que.push(x_dot);
                    visited[x_dot] = true;
                    count += 1;
                    //printf("%d ", x_dot);
                }
            }        
        }
    }
    int answer = (n-2*count >= 0) ? n-2*count : 2*count-n;
    return answer;
      
}

int solution(int n, vector<vector<int>> wires) {
    int answer = n;
    for (int i=0; i <= wires.size(); i++) {
        answer = min(answer, bfs(n,i,wires));
    }
    return answer; 
}

//끊고 모든 경우에서 bfs
//두개로 나눠지니까 1부터 한번만 해보면 됨