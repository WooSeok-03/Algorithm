#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> arr, int divisor) {
    vector<int> answer;
    
    for(int i = 0; i < arr.size(); i++)
    {
        if(arr[i] % divisor == 0)
        {
            answer.push_back(arr[i]);
        }
    }
    
    if(answer.empty())
    {
        answer.push_back(-1);
    }
    
    sort(answer.begin(), answer.end());	// <algorithm>헤더파일에 있는 sort()함수 
    
    return answer;
}

// sort()함수
// 3번째 인자를 넣지 않으면 default로 오름차순으로 정렬
// 3번째 인자를 사용하면 사용자가 정의한 함수를 기준으로 정렬을 할 수 있다.