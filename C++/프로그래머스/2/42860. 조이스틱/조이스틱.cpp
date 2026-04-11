#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int ShortestPath(const string& name) { //제일 긴 A를 찾아라
    int n = name.length();
    int path = n-1;
    for (int i=0; i < n; i++) {
        int next_idx = i+1;
        while (next_idx < n && name[next_idx] == 'A') { //string의 특정 인덱스는 char이고 "A"는 string으로 처리됨 
            next_idx++;
        }
        int distance = i + n - next_idx + min(i, n - next_idx);
        path = min(path, distance);            
    }
    return path;
}

int solution(string name) {
    int answer = ShortestPath(name);
    printf("%d", answer);
    for (int i=0; i < name.length(); i++) 
        answer += min(name[i] - 'A',26 + 'A' - name[i]);
    return answer;
}

//vector.length(), string.size()의 반환형은 모두 size_t 이다!