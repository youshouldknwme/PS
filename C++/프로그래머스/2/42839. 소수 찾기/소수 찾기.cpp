#include <string>
#include <vector>

using namespace std;

bool used[1000001]; 

bool isPrime(int num) {
    if (num <= 1)
        return false;
    for (int i=2; i < num ; i++) {
        if (num%i == 0)
            return false;
    }
    return true;
}

int pow(int n, int r,int cur) {
    if (r==0)
        return cur;
    return pow(n,r-1,cur*n);
}
int F(int total, int depth, vector<int> n, int erase) {
    int answer = 0;
    n.erase(n.begin()+erase); //erase 번째 원소를 지우고 싶을 때!
    for (int i=n.size()-1; i >= 0; i--) {
        int sum = n[i]*pow(10,depth,1);
        total += sum;
        if (isPrime(total) && !used[total]) {
            answer += 1;
            used[total] = true;
            printf("%d ",total);
        }
        answer += F(total,depth+1,n,i); //cal by value로 하면 안 지운 것처럼 가능
        total -= sum;
    }
    return answer;
}

int solution(string numbers) {
    int answer = 0;
    vector<int> n;
    for (int i=0; i < numbers.length(); i++)
        n.push_back(numbers[i]-'0');
    n.push_back('0');
    answer = F(0,0,n,n.size()-1);
    return answer;
}