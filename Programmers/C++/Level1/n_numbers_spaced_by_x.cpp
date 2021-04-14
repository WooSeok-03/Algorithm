#include <string>
#include <vector>

using namespace std;

vector<long long> solution(int x, int n) {
    vector<long long> answer;
    
    for(int i = 1; i < n+1; i++)
    {
        answer.push_back(i*x);	// push_back() 함수 : 가장뒤에 인자 추가
    }
    
    return answer;
}