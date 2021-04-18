#include <string>
#include <vector>

using namespace std;

// 최대 공약수를 구하는 함수
int gcd(int a, int b)
{
    return b ? gcd(b, a%b) : a; // 유클리드 호제법 사용
}

vector<int> solution(int n, int m) {
    vector<int> answer;
    
    answer.push_back(gcd(n, m));
    answer.push_back(n * m / gcd(n, m));    // 최소 공배수를 구하는 식 : n * m / gcd(n,m)
    
    return answer;
}

