#include <string>
#include <vector>

using namespace std;

bool solution(int x) {
    bool answer = true;
    int n = x;
    int num = 0;
    int result = 0;
    
    while(n != 0)
    {
        num = n % 10;
        n /= 10;
        result += num;
    }
        
    if((x % result) == 0) answer = true;
    else answer = false;
    
    return answer;
}