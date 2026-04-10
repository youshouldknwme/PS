#include <string>
#include <vector>
#include <algorithm>

using namespace std;



int dfs(int k,vector<bool>& visited,const vector<vector<int>>& dungeons) {
    int answer = 0;
    for (int i=0; i < dungeons.size(); i++) {
        if (!visited[i] && k >= dungeons[i][0]) {
            visited[i] = true;
            answer = max(answer, 1+ dfs(k-dungeons[i][1],visited, dungeons));
            visited[i] = false;
        }
    }
    return answer;
}

int solution(int k, vector<vector<int>> dungeons) {
    int answer = -1;
    vector<bool> visited(dungeons.size(),false);
    answer = dfs(k,visited,dungeons);
    return answer;
}

//dfs로 브루트포스