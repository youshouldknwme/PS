#include <string>
#include <vector>
#include <algorithm>

using namespace std;

long long solution(int n, vector<int> times) {
    long long answer = 0;
    sort(times.begin(),times.end());
    long long max_T= (long long)times.back() * n; //time이 이 범위를 넘길 수 없다
    long long min_T = 1;
    while (min_T < max_T) {
        long long mid_T = (max_T+min_T)/2;
        long long count = 0; 
        for (int time : times) {
            count += mid_T/time;
            if (count > n) //더 이상 계산필요 x
                break;
        }
        (count >= n) ? max_T =mid_T : min_T = mid_T+1;    
    }
    return answer = min_T;
}


// 제일 긴 대기 시간 * n 으로부터 시작!