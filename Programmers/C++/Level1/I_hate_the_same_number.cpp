#include <vector>
#include <iostream>
// #include <algorithm>		// unique()함수를 사용하기 위해 필요

using namespace std;

vector<int> solution(vector<int> arr) 
{
    vector<int> answer;

    for(int i = 0; i < arr.size(); i++)
    {
        if(i+1 >= arr.size() && arr[i] < 1) answer.push_back(arr[i]);
        if(arr[i] != arr[i+1]) answer.push_back(arr[i]);
    }

    return answer;
}

//vector<int> solution(vector<int> arr) 
//{
//    return arr.erase(unique(arr.begin(), arr.end()), arr.end());
//}

// unique()는 연속된 중복 원소를 vector의 제일 뒷부분으로 보낸다.
// erase()는 첫번째 파라미터부터 두번째 파라미터까지의 인자를 삭제한다.
// 따라서 arr.erase(unique(arr.begin(), arr.end()), arr.end());를 사용하면 vector의 중복된 요소를 없앨 수 있다.