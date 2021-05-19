#include <string>
#include <vector>
#include <algorithm>

using namespace std;

// string 변환 후, 뒤집어서 다시 int로 변환 후, 배열에 삽입
vector<int> solution(long long n) {
    vector<int> answer;
    
    string str_n = to_string(n);
    reverse(str_n.begin(), str_n.end());
    
    for(int i = 0; i < str_n.size(); i++)
    {
        int num = (int)str_n[i] - '0';
        answer.push_back(num);
    }
    
    return answer;
}

/*
vector<int> solution(long long n) {
    vector<int> answer;
    
    while(n)
    {
        answer.push_back(n%10);
        n /= 10;
    }
    
    return answer;
}
*/