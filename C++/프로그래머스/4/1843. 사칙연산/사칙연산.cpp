#include <vector>
#include <string>
using namespace std;

int DP(const vector<string>& arr) { //ismax 최대값
    vector<vector<pair<int,int>>> dp(arr.size());
    for (auto& v : dp)
        v.resize(arr.size());
    for (int i = arr.size()-1; i >= 0; i-=2) {
        for (int j = i; j <= arr.size()-1; j+=2) {
            if (i==j) {
                dp[i][j] = make_pair(stoi(arr[i]),stoi(arr[i]));
                continue;
            }
            int min_num = 101*1000+1,max_num = -101*1000-1;
            for (int k=i+1; k < j; k+= 2) {
                if (arr[k] == "+") {
                    min_num = min(min_num,dp[i][k-1].first + dp[k+1][j].first);
                    max_num = max(max_num,dp[i][k-1].second + dp[k+1][j].second);
                }
                else {
                    min_num = min(min_num,dp[i][k-1].first - dp[k+1][j].second);
                    max_num = max(max_num,dp[i][k-1].second - dp[k+1][j].first);
                }
            dp[i][j] = make_pair(min_num,max_num);
            }
        }
    } 
    return dp[0][arr.size()-1].second;
}

int solution(vector<string> arr)
{
    int answer = -1;
    answer = DP(arr);
    return answer;
}