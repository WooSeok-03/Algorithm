#include <string>
#include <vector>

using namespace std;

long long solution(int a, int b) {
    long long answer = 0;
    int low, high;
    
    if(a < b)
    {
        low = a;
        high = b;
    }
    else
    {
        low = b;
        high = a;
    }
    
    for(int i = low; i <= high; i++)
    {
        answer += i;
    }
    
    return answer;
}