#include <string>
#include <vector>
#include <queue> //bfs 구현

using namespace std;

int solution(vector<int> numbers, int target) {
    int answer = 0;
    int sign[2] = {-1,1};
    //queue<vector<int>> que = {{0,0}}; error! std:queue에선 직접 넣을 수 없음 
    queue<vector<int>> que;
    que.push({0,0});
    while (!que.empty()) {
        int i = que.front()[0], sum = que.front()[1];
        que.pop();
        if (i != numbers.size()) { //아직 전체 계산 x
            for (int j=0; j !=2; j++) {
                que.push({i+1,sum+numbers[i]*sign[j]});
                }
            }
        
        else { //끝까지 다 계산했으므로 target과 비교
            if (sum == target) 
                answer = answer + 1;
            
        }
    }
    return answer;
}