#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> arr) {
    vector<int> a;
    
    if(arr.size() < 2)
    {
        a.push_back(-1);
        return a;
    }
    
    a = arr;
    sort(a.begin(), a.end());
    
    for(int i = 0; i < arr.size(); i++)
    {
        if(arr[i] == a[0])
        {
            arr.erase(arr.begin() + i);
        }
    }
    
    return arr;
}

/*
vector<int> solution(vector<int> arr) {
    if(arr.size() < 2)
    {
        vector<int>a(1, -1);
        return a;
    }
    
    int min_value = *min_element(arr.begin(), arr.end());	
    int position = find(arr.begin(), arr.end(), min_value) - arr.begin();	
    arr.erase(arr.begin() + position);
    
    return arr;
}
*/

// *min_element()는 첫번째 파라미터부터 두번째 파라미터까지 탐색하여 가장 작은 수를 반환한다.
// +) *max_element()는 첫번째 파라미터부터 두번째 파라미터까지 탐색하여 가장 큰 수를 반환한다.
// 앞에 '*'을 붙이는 이유는 C++에서는 배열 역시 array라는 클래스형 객체로 취급하기 때문이다.

// find()는 첫번째 파라미터부터 두번째 파리미터까지 탐색하여 셋번째 파라미터가 어느 인덱스에 있는지 반환한다.
// ( 반환값은 첫 번째로 일치하는 원소를 가리키는 반복자이고, 일치하지 않다면 두번째 파라미터를 반환한다. )