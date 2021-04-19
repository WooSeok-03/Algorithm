#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(string s) {
    sort(s.begin(), s.end(), greater<int>());   
    return s;
}

// sort()에서 3번째 파라미터에 "greater<자료형>()"을 넣어주면 내림차순으로 정렬한다.