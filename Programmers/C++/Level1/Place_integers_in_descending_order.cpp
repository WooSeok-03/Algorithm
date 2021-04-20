#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

long long solution(long long n) {
    long long answer = 0;
    string temp = to_string(n);
    sort(temp.begin(), temp.end(), greater<int>());
    answer = stoll(temp);
    
    return answer;
}

// sort()의 세번째 파라미터에 greater<int>()를 넣어주면 내림차순으로 정렬된다.
// stoll()은 string변수를 long long형으로 바꿀 수 있다.