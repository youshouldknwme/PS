#include <string>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

bool compare_cost(vector<int> a,vector<int> b) {
    if (a[2] <= b[2])
        return true;
    return false;
}

bool isConnected(int a,int b, const vector<vector<int>>& graph) {
    vector<bool> visited(graph.size(),false);
    queue<int> que;
    que.push(a);
    visited[a] = true;
    while (!que.empty()) {
        int x = que.front();
        que.pop();
        for (const auto& v : graph[x]) {
            if (!visited[v]) {
                que.push(v);
                visited[v] = true;
            }
        }
    }
    return visited[b];
}

bool isAllConnected(const vector<vector<int>>& graph) { //
    vector<bool> visited(graph.size(),false);
    queue<int> que;
    que.push(0);
    visited[0] = true;
    int count = 1;
    while (!que.empty()) {
        int x = que.front();
        que.pop();
        for (const auto& v : graph[x]) {
            if (!visited[v]) {
                que.push(v);
                count++;
                visited[v] = true;
            }
        }
    }
    return count == graph.size();
}

    


int solution(int n, vector<vector<int>> costs) {
    int answer = 0;
    vector<vector<int>> graph(n);
    vector<int> visited(n);
    sort(costs.begin(),costs.end(),compare_cost);
    for (auto cost : costs) {
        int start = cost[0], end = cost[1], c=cost[2];
        if (isConnected(start,end,graph))
            continue;
        graph[start].push_back(end);
        graph[end].push_back(start);
        answer += c;
        if (isAllConnected(graph))
            break;
    }
    return answer;
}



//cycle 상관 없으므로 작은 간선부터 넣는 식으로 하고 두 간선이 이미 방문됐으면 